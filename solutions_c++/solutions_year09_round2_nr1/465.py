//Jakub Sygnowski
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <sstream>
#define PB push_back
#define LL long long 
#define REP(I,N) for(int I=0;I<(N);I++)
using namespace std;
string getline(){
	string s;
	char zn;
	while(!feof(stdin)){
		zn=fgetc(stdin);
		if (zn==13) continue;
		if (zn=='\n') return s;
		if (zn=='('||zn==')')
			s+=' ';
		s+=zn;
		if (zn=='('||zn==')')
			s+=' ';
	}
	return s;
}
int getnr(){
	return atoi(getline().c_str());
}
struct drz{
	string fea;
	long double numb;
};
map<LL,drz> tab;
map<string,bool> ma;
void rek(LL x);
string opis,op2,nazw;
long double pkt,p;
int t,lin,zw,cech;
long long gdzie;
istringstream iss;
char sm[1000];
FILE *temp,*tempa;
int main(){
	t=getnr();
	REP(nr,t){
		temp=fopen("temp.txt","w");
		printf("Case #%d:\n",nr+1);
		opis.clear();
		lin=getnr();
		tab.clear();
		while(lin--) opis+=getline();
		fprintf(temp,"%s\n",opis.c_str());
		fclose(temp);
		tempa=fopen("temp.txt","r");
//		printf("%s\n",opis.c_str());
		fscanf(tempa,"%s",sm);
		rek(1LL);
		/*for(int i=1;i<10;i++){
			printf("%Lf %s\n",tab[i].numb,tab[i].fea.c_str());
		}*/
		zw=getnr();
		while(zw--){
			op2=getline();
			istringstream iss(op2);
			iss>>nazw; //nazwa - smiec
			ma.clear();
			iss>>cech;
			while(cech--){
				iss>>nazw;
				ma[nazw]=true;
			}
			p=1.0;
			gdzie=1LL;
			while(!tab[gdzie].fea.empty()){
			//	printf("%d\n",gdzie);
				p*=tab[gdzie].numb;
				gdzie*=2;
				if (ma.find(tab[gdzie/2].fea)==ma.end())
					gdzie++;
			}
		//	printf("%d\n",gdzie);
			p*=tab[gdzie].numb;
			printf("%.7Lf\n",p);
		}
	}
}
void rek(long long x){
	
	fscanf(tempa,"%Lf",&pkt);

//	printf("%lf\n",pkt);
	tab[x].numb=pkt;
	fscanf(tempa,"%s",sm);
	nazw=sm;
//	printf("%d %lf %s\n",x,pkt,nazw.c_str());
	if (nazw==")") return;
	tab[x].fea=nazw;
	fscanf(tempa,"%s",sm); //smiec
	rek(2*x);
	fscanf(tempa,"%s",sm);
	rek(2*x+1);
	fscanf(tempa,"%s",sm); //smiec
}
