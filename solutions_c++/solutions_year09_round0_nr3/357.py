#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
#define MODV 10000
//'welcome to code jam'
//'0123456789012345678'

int val[19]; //w e l c o m B t d j a  
char line[1001];
void doita(int x){
	if(x==0){
		val[0]=(val[0]+1)%MODV;
		return;
	}
	val[x]=(val[x]+val[x-1])%MODV;
	return;

}
void doit(){
	int len;
	memset(val,0,sizeof(val));
	cin.getline(line,1001);
	len=strlen(line);
	for(int i=0;i<len;i++){
		if(line[i]=='w'){doita(0);}
		else if(line[i]=='e'){doita(1);doita(6);doita(14);}
		else if(line[i]=='l'){doita(2);}
		else if(line[i]=='c'){doita(3);doita(11);}
		else if(line[i]=='o'){doita(4);doita(9);doita(12);}
		else if(line[i]=='m'){doita(5);doita(18);}
		else if(line[i]==' '){doita(7);doita(10);doita(15);}
		else if(line[i]=='t'){doita(8);}
		else if(line[i]=='d'){doita(13);}
		else if(line[i]=='j'){doita(16);}
		else if(line[i]=='a'){doita(17);}
	}
	printf("%04d\n",val[18]);
	return;
}
int main(){
	int tc;
	cin.getline(line,1001);
	tc=atoi(line);
	for(int i=1;i<=tc;i++){
		cout<<"Case #"<<i<<": ";
		doit();
	}
	return 0;
}
