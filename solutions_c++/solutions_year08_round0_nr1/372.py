#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void sort( char arr[][100], int size)
{
 	for (int i=1; i<size; i++){
		for(int j=0; j<i; j++){
			if(strcmp(arr[i], arr[j])<0){
				char tmp[100];
				strcpy(tmp, arr[i]);
				strcpy(arr[i], arr[j]);
				strcpy(arr[j], tmp);
			}
				
		}
	}
}

int find(char arr[][100], int size, char req[])
{
	int first=0; int last = size;
	while(first<last-1){
		int c = (first+last)/2;
		int res =strcmp(arr[c], req);
		if(res==0){
			return c;
		}else{
			if(res<0){
				first = c;	
			}else {
				last = c;
			}
		}
	}
	if(strcmp(arr[first], req)==0) return first;
	if(strcmp(arr[last], req)==0) return last;
	return -1;
}

int main () {
	//string line;
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; i++){
		int nengines;
		cin >> nengines; cin.get();
		char  engines[nengines+1][100];
		for(int j=0; j<nengines; j++){
			cin.getline( engines[j], 100);
			//cin >> engines[j]; cin.get();
		}
		sort(engines, nengines);
		for(int j=0; j<nengines; j++){
			//cout << engines[j] <<"\n";
		}
		int nrequests;
		cin >> nrequests;
		cin.get();
		//cout << nrequests;
		int c = 0;
		int nswitch = 0;
		char ethalon[100];
		memset(ethalon,'1', nengines);
		ethalon[nengines] =0;
		
		char request[100];
		int eng =-1;
		//cout<<ethalon<<"wwww\n";
		while(c<nrequests){
			char teststr[100];
			memset( teststr, '0', nengines);
			teststr[nengines]=0;
			if(eng>=0)teststr[eng] = '1';
			do{
				cin.getline( request, 100);
				//cin >> request;
				eng = find(engines, nengines, request );
				if(eng>=0)	teststr[eng]='1';
				//cout<<teststr<<"eee\n";
//				set_char_in_teststr(teststr, request);
				c++;
			}while(c<nrequests && strcmp(teststr, ethalon)!=0);
			if(strcmp(teststr, ethalon)==0)nswitch++;
		} 
		cout <<"Case #"<<i<<": "<< nswitch<<"\n";
	}
}