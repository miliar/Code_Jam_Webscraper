#include <iostream>
#include <queue>

using namespace std;

enum events { A_ARRIVAL , B_ARRIVAL , A_DEPARTURE , B_DEPARTURE };


int main(int argc , char *argv)
{

	priority_queue<int,vector<int>,greater<int> > pque;
	int N,T,NA,NB;
	string str1="",str2="",str3="",str4="";
	int num1,num2;
	int counta = 0 ; int countb = 0;

	cin >> N;
	for ( int n = 0 ; n < N ; n++ )
	{
       counta = 0 ;
	   countb = 0 ;

		cin >> T;
		cin >> NA;
		cin >> NB;

		for ( int na = 0 ; na < NA ; na++ )
		{
			str1 = "";
			str2 = "";
			str3 = "";
			str4 = "";

			getline(cin,str1,':');
			getline(cin,str2,' ');
			getline(cin,str3,':');
			getline(cin,str4,'\n');

			num1 = ( atoi(str1.c_str()) * 60 + atoi(str2.c_str() ) ) * 10 + A_DEPARTURE ;
			num2 = ( atoi(str3.c_str()) * 60 + atoi(str4.c_str() ) + T ) * 10 + B_ARRIVAL ;

	        pque.push(num1);
	        pque.push(num2);		


		}

		for ( int nb = 0 ; nb < NB ; nb++ )
		{
			str1 = "";
			str2 = "";
			str3 = "";
			str4 = "";

			getline(cin,str1,':');
			getline(cin,str2,' ');
			getline(cin,str3,':');
			getline(cin,str4,'\n');

			num1 = ( atoi(str1.c_str()) * 60 + atoi(str2.c_str() ) ) * 10 + B_DEPARTURE ;
			num2 = ( atoi(str3.c_str()) * 60 + atoi(str4.c_str() ) + T ) * 10 + A_ARRIVAL ;

			pque.push(num1);
			pque.push(num2);		


		}

		
		queue <int> stationa;
		queue <int> stationb;

		while ( ! pque.empty() )
		{
			int num = pque.top();
            
			int event = num % 10;
			int time = num / 10;

            switch ( event )
			{
				case A_DEPARTURE: 
					if ( stationa.empty() )
					{
						counta++;
					}
					else
					{
					   stationa.pop();
				    }
			      break;

		      case B_DEPARTURE:
		         		if ( stationb.empty() )
					{
						countb++;
					}
					else
					{
					   stationb.pop();
				    }
			      break;

			  case A_ARRIVAL:
				  stationa.push(num);
				  break;

			  case B_ARRIVAL:
				  stationb.push(num);
				  break;

			  default : cout << "Some error" << endl;	  
	  


			}


			pque.pop();
		}


		cout << "Case #" << n+1 << ": " << counta << " " << countb << endl;


	} // end of loop n ( Test case )




}
