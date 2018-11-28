#include <string>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
int main(){
	/*string l;
	string a;
	vector<bool> v('z'-'a'+1,false);
	set<pair<int,char> > S;
	while(getline(cin,l)!=NULL){
		cout<<l<<endl;
		getline(cin,a);
		for(int i=0;i<l.size();i++){
			if(l[i]!=' '){
				v[l[i]-'a']=true;
				S.insert(make_pair(a[i]-'a',l[i]));
			}
		}
	}
	for(set<pair<int,char> >::iterator it=S.begin();it!=S.end();it++){
		cout<<"r["<<(*it).first<<"]='"<<(*it).second<<"';"<<endl;
	}
	*/
	char r[26];
	r[0]='y';
r[1]='h';
r[2]='e';
r[3]='s';
r[4]='o';
r[5]='c';
r[6]='v';
r[7]='x';
r[8]='d';
r[9]='u';
r[10]='i';
r[11]='g';
r[12]='l';
r[13]='b';
r[14]='k';
r[15]='r';
r[16]='z';
r[17]='t';
r[18]='n';
r[19]='w';
r[20]='j';
r[21]='p';
r[22]='f';
r[23]='m';
r[24]='a';
r[25]='q';
	int caso=0;
	string linea;
	int numCasos;
	scanf("%d\n",&numCasos);
	while(numCasos--){
		getline(cin,linea);
		//cout<<linea<<endl;
		printf("Case #%d: ",++caso);
		for(int i=0;i<linea.size();i++){
			if(linea[i]==' ') printf(" ");
			else
			printf("%c",r[linea[i]-'a']);
		}
		cout<<endl;
	}
return 0;}
