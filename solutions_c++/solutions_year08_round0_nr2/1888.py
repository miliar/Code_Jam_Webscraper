#include <iostream>
#include <vector>
#include <stack>
#include <math.h>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <fstream>
using namespace std ;

vector<float> AStation ;
vector<float> BStation ;

vector<struct Trip> ASchedule ;
vector<struct Trip> BSchedule ;

int TrainsInAstation[80] ;
int TrainsInBstation[80] ;

int needA = 0 , needB =  0 ;

int NA = 0 , NB = 0 ;	
float turnInMin ;
float T ;

struct Trip
{
	float departure ;
	float arrival ;
};

int findIndex(vector<float> v , float value)
{
	int low = 0 , high = v.size() - 1 ;
	int mid = -1  , i = 0;
	while( low <= high)
	{
		mid = (low + high) / 2 ;
		if( v[mid] == value)
		{		
			return mid ;
		}
		else 
		{
			if(v[mid] > value)
			{
				high = mid - 1 ;
			}
			else
			{
				low = mid + 1 ;
			}
		}
	}
	return -1 ;
}

void RunA(int& Aindex)
{	
	int dex = findIndex(AStation ,ASchedule[Aindex].departure ) ;
	if(dex != 0)
	{
		for(int i = dex - 1 ; i >= 0 ; -- i)
		{
			TrainsInAstation[dex]  += TrainsInAstation[i] ;
			TrainsInAstation[i] = 0 ;
		}		
	}
	if(TrainsInAstation[dex] == 0 )
	{
		needA ++ ;				
	}
	else
	{
		TrainsInAstation[dex]  --  ;	
	}
	int arrivalIndex = findIndex( BStation ,ASchedule[Aindex].arrival + turnInMin );
	if(arrivalIndex != -1)
	{
		TrainsInBstation[arrivalIndex] ++ ;
	}	
}

void RunB(int& Bindex)
{
	int dex = findIndex(BStation ,BSchedule[Bindex].departure ) ;
	if(dex != 0)
	{
		for(int i = dex - 1 ; i >= 0 ; -- i)
		{
			TrainsInBstation[dex]  += TrainsInBstation[i] ;
			TrainsInBstation[i] = 0 ;
		}
	}
	if(TrainsInBstation[dex] == 0 )
	{
		needB ++ ;				
	}
	else
	{
		TrainsInBstation[dex]  --  ;	
	}
	int arrivalIndex = findIndex( AStation ,BSchedule[Bindex].arrival + turnInMin);
	if(arrivalIndex != -1)
	{
		TrainsInAstation[arrivalIndex] ++ ;
	}

}

void Process()
{	
	int Aindex = 0  , Bindex = 0 ;
	needA = 0 ;
	needB = 0 ;
	memset(TrainsInAstation , 0 , sizeof(TrainsInAstation) );
	memset(TrainsInBstation , 0 , sizeof(TrainsInBstation));
	while( Aindex < ASchedule.size() || Bindex < BSchedule.size())
	{
		if( Aindex < ASchedule.size() && Bindex < BSchedule.size())
		{
			if( ASchedule[Aindex].departure < BSchedule[Bindex].departure )
			{
				RunA(Aindex) ;
				Aindex ++ ;
			}
			else
			{
				RunB(Bindex);
				Bindex ++ ;
			}
			continue ;
		}
		if( Aindex >= ASchedule.size())
		{
			RunB(Bindex) ;
			Bindex ++ ;
			continue ;
		}
		if(Bindex >= BSchedule.size())
		{
			RunA(Aindex) ;
			Aindex ++ ;
		}

	}
}


struct Trip ToTrpTime(string line)
{
	struct Trip _time ;
	_time.departure = 0.0f ;
	_time.arrival = 0.0f ;
	_time.departure +=  (float)(atoi(line.substr(0, 2).c_str() ));
	_time.departure +=  (float)(atoi(line.substr(3, 2).c_str()))/ 60.f;

	int spaceIndex = line.find(' ');
	_time.arrival += (float)(atoi(line.substr(spaceIndex + 1, 2).c_str() ) );
	_time.arrival += (float)(atoi(line.substr(spaceIndex + 4, 2).c_str() ) )/ 60.f;

	return _time ;
}

bool UDLess ( struct Trip elem1, struct Trip elem2 )
{
	return elem1.departure < elem2.departure;
}

void DeleteSameElement(vector<float>& v)
{
	vector<float> tmp;
	if(v.size() == 0)
		return ;
	tmp.push_back(v[0]);
	float prev = v[0] ;
	for( int i = 1 ; i < v.size() ; ++ i )
	{
		if( v[i] != prev)
		{
			prev = v[i] ;
			tmp.push_back(v[i]) ;
		}
	}

	v.clear();
	
	for(int i = 0 ; i < tmp.size() ; ++ i)
	{
		v.push_back(tmp[i]) ;
	}
}

void FillStationInform()
{
	for( int i = 0 ; i < ASchedule.size() ; ++ i)
	{
		AStation.push_back(ASchedule[i].departure) ;
		BStation.push_back(ASchedule[i].arrival + turnInMin) ;
	}

	for( int i = 0 ; i < BSchedule.size() ; ++ i)
	{
		BStation.push_back(BSchedule[i].departure) ;
		AStation.push_back(BSchedule[i].arrival + turnInMin) ;
	}

	sort( AStation.begin() , AStation.end());
	sort( BStation.begin() , BStation.end());

	DeleteSameElement(AStation) ;
	DeleteSameElement(BStation) ;
}

int main()
{
	int N = 0 , round = 1;
	ofstream outfile ;
	outfile.open("c://output.txt") ;
	cin >> N ;
	while( N --)
	{
		cin >> T ;
		turnInMin = T / 60.0f ;

		cin >> NA >> NB ;
		string temp ;
		getline( cin , temp);
		
		for( int i = 0 ; i < NA ; ++ i)
		{
			getline( cin , temp);
			ASchedule.push_back(ToTrpTime(temp)) ;			
		}

		for( int i = 0 ; i < NB ; ++ i)
		{
			getline( cin , temp);
			BSchedule.push_back(ToTrpTime(temp)) ;			
		}
		
		sort(ASchedule.begin() , ASchedule.end() ,UDLess);
		sort(BSchedule.begin() , BSchedule.end(), UDLess);

		FillStationInform() ;
		Process();

		outfile << "Case #"<< round ++ <<": " << needA <<" "<< needB << endl ;
		
		ASchedule.clear() ;
		BSchedule.clear();
		AStation.clear() ;
		BStation.clear();
		
	}
	outfile.close() ;
} 