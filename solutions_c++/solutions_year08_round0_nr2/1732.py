#ifndef __IOSTREAM__ 
#define __IOSTREAM__
#include <iostream>
#include <fstream>
#include <Vector>
#endif

using namespace std;

#define FILENAME  "B-large.in"

int timecomp( string a, string b ) {
	char sa[2], sb[2];
	strcpy(sa,a.substr(0,2).c_str());
	strcpy(sb,b.substr(0,2).c_str());
	if ( strcmp( sa,sb ) != 0 ) 
		return strcmp( sa,sb );
	strcpy(sa,a.substr(3,2).c_str());
	strcpy(sb,b.substr(3,2).c_str());
	return strcmp( sa,sb );
}

void sort( vector<string>* trains, vector<string>* trains_end ) {

	string train;
	int k=1;
	for ( int i=(*trains).size()-1; i > 0; i-- ) {
		for ( int j=(*trains).size()-1; j >= (*trains).size()-i; j-- ) {
			if( timecomp((*trains)[j],(*trains)[j-1])<0 ) {
				train = (*trains)[j-1];
				(*trains)[j-1] = (*trains)[j];
				(*trains)[j] = train;
				train = (*trains_end)[j-1];
				(*trains_end)[j-1] = (*trains_end)[j];
				(*trains_end)[j] = train;
			}
		}
	}
}

void sort( vector<string>* trains, vector<int>* trains_end ) {

	string train;
	int k=1;
	int n;
	for ( int i=(*trains).size()-1; i > 0; i-- ) {
		for ( int j=(*trains).size()-1; j >= (*trains).size()-i; j-- ) {
			if( timecomp((*trains)[j],(*trains)[j-1])<0 ) {
				train = (*trains)[j-1];
				(*trains)[j-1] = (*trains)[j];
				(*trains)[j] = train;
				n = (*trains_end)[j-1];
				(*trains_end)[j-1] = (*trains_end)[j];
				(*trains_end)[j] = n;
			}
		}
	}
}

bool able( string stime, vector<string> endtime, int time, vector<bool>* flag ) {
	
	char temp[5];
	int min,hour;
	vector<string> max;
	vector<int> num;
	bool bflag = false;

	for ( int i=endtime.size()-1; i>=0; i-- ){

		strcpy(temp,endtime[i].c_str());
		min = (temp[3]-48)*10 + temp[4]-48 + time;
		hour = (temp[0]-48)*10 + temp[1]-48;
		if (min>=60) {
			min = min%60;
			hour = hour+1;
			temp[1]=hour%10+48;
			temp[0]=(hour-hour%10)/10+48;
		}
		temp[4]=min%10+48;
		temp[3]=(min-min%10)/10+48;

		if (timecomp(stime,temp)>=0 && !(*flag)[i] ) {
			max.push_back(temp);
			num.push_back(i);
			bflag=true;
		}
	}

	if ( bflag ) {
		sort(&max,&num);
		(*flag)[num[num.size()-1]]=true;
		return true;
	}

	return false;
}

void remove( vector<string>* temp, int n) {
	for ( int i=n; i<(*temp).size()-1; i++ ) {
		(*temp)[i-1]=(*temp)[i];
	}
	(*temp).pop_back();
}

void remove( vector<bool>* temp, int n) {
	for ( int i=n; i<(*temp).size()-1; i++ ) {
		(*temp)[i-1]=(*temp)[i];
	}
	(*temp).pop_back();
}

void main(){

	int n,i,j,k;
	int time;
	int num;
	int temp;
	int flag;

	ifstream file(FILENAME,ios::in);
	if(file.fail()){
		file.close();
		system("pause");
		exit(0);
	} 
	ofstream ouputfile("output.txt",ios::out);


	file>>n;
	vector<string> A_S;
	vector<string> A_E;
	vector<string> B_S;
	vector<string> B_E;
	vector<bool> A_F;
	vector<bool> B_F;
	string stemp;
	char a[100] = "";
	char b[100] = "";

	for ( int casenum = 0; casenum < n; casenum++ ) {
		A_S.clear();
		A_E.clear();
		B_S.clear();
		B_E.clear();
		A_F.clear();
		B_F.clear();
		file>>time;
		file>>i;
		file>>j;

		if ( i==0 || j==0 ){
			ouputfile<<"Case #"<<casenum+1<<": "<<i<<" "<<j<<endl;
			continue;
		}

		for ( k = 0; k < i; k++ ) {
			file>>a;
			stemp = a;
			A_S.push_back(a);
			file>>a;
			stemp = a;
			A_E.push_back(a);
			A_F.push_back(false);
		}
		for ( k = 0; k < j; k++ ) {
			file>>b;
			stemp = b;
			B_S.push_back(b);
			file>>b;
			stemp = b;
			B_E.push_back(b);
			B_F.push_back(false);
		}

		sort( &A_S, &A_E );
		sort( &B_S, &B_E );
		
		int anum=1,bnum=1;

		while( !(anum>A_S.size()&&bnum>B_S.size()) ) {
			if ( A_S.size()==0 || B_S.size()==0 ){
				break;
			}
			if ( anum>A_S.size() ) {

				if (able( B_S[B_S.size()-bnum], A_E, time, &A_F )) {
					remove(&B_S,B_S.size()-bnum);
					remove(&B_E,B_E.size()-bnum);
					remove(&B_F,B_F.size()-bnum);
				} else {
					bnum++;
				}

			} else if ( bnum>B_S.size() ) {

				if (able( A_S[A_S.size()-anum], B_E, time, &B_F )) {
					remove(&A_S,A_S.size()-anum);
					remove(&A_E,A_E.size()-anum);
					remove(&A_F,A_F.size()-anum);
				} else {
					anum++;
				}

			} else if( timecomp(A_S[A_S.size()-anum],B_S[B_S.size()-bnum])>=0 ) {

				if (able( A_S[A_S.size()-anum], B_E, time, &B_F )) {
					remove(&A_S,A_S.size()-anum);
					remove(&A_E,A_E.size()-anum);
					remove(&A_F,A_F.size()-anum);
				} else {
					anum++;
				}

			} else {

				if (able( B_S[B_S.size()-bnum], A_E, time, &A_F )) {
					remove(&B_S,B_S.size()-bnum);
					remove(&B_E,B_E.size()-bnum);
					remove(&B_F,B_F.size()-bnum);
				} else {
					bnum++;
				}

			}
		}

		ouputfile<<"Case #"<<casenum+1<<": "<<A_S.size()<<" "<<B_S.size()<<endl;
	}

	ouputfile.close();
	file.close();
}
