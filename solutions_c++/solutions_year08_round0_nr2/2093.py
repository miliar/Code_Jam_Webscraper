#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

class tiempo{

public:
	int hor,mins;

public:
	tiempo(){
	}
	tiempo(int _hor,int _mins):hor(_hor),mins(_mins){
	}
	
	bool menor(tiempo t){

			if(hor!=t.hor)
		return hor<t.hor;
			else
		return mins<t.mins;
	

	}
	void sum(int mint){

		int aux=mins+mint;
		if((aux)<60){

			mins=aux;

		}

		else{

			hor++;
			mins=aux%60;

		}
	}


};

class trip{

public:
	tiempo sal,lleg;
	int dir;
public:
	trip(){
	}
void set_trip(tiempo sale,tiempo llega,int d){

	sal=sale;
	lleg=llega;
	dir=d;

	}

};

class tren {

public:
	tiempo lleg;
	int dir;
public:
	tren(){
	}
	tren(tiempo _lleg,int _dir):lleg(_lleg),dir(_dir){
	}


};


bool cmp( trip a,trip b ) {
	
	if(a.sal.hor!=b.sal.hor)
		return a.sal.hor<b.sal.hor;
	else
		return a.sal.mins<b.sal.mins;
	
 }  

bool posible (trip v,vector <tren> &t){

	for(int i=0;i<t.size();++i){

		if(t[i].dir!=v.dir){

			if(!v.sal.menor(t[i].lleg)){
				t.erase(t.begin()+i);
				t.push_back(tren(v.lleg,v.dir));
				return true;
			}
		}

	}

	return false;
}

int answer(vector<trip> trips,int u){

	vector <tren> t;
	int cont1=0,cont2=0;
	std::sort(trips.begin(),trips.end(),cmp);

	if(trips.size()==0){
		printf("Case #%d: 0 0\n",u);
		return 0;
	}

	t.push_back(tren(trips[0].lleg,trips[0].dir));
	if(trips[0].dir==0)cont1++;
	else cont2++;
	for(int i=1;i<trips.size();++i){

	
		if(!posible(trips[i],t)){
			t.push_back(tren(trips[i].lleg,trips[i].dir));
			if(trips[i].dir==0)cont1++;
			else cont2++;
						
		}


	}

	printf("Case #%d: %d %d\n",u,cont1,cont2);

	return 0;


}

void main(){

	int n,t,na,nb,h1,h2,m1,m2,res;
	vector <trip >trips;
	trip aux;


	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	scanf("%d",&n);
	for(int i=1;i<=n;i++){


		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(int j=0;j<na;j++){

			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			aux.set_trip(tiempo(h1,m1),tiempo(h2,m2),0);
			aux.lleg.sum(t);
			trips.push_back(aux);
		}

		for(int j2=0;j2<nb;j2++){

			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			aux.set_trip(tiempo(h1,m1),tiempo(h2,m2),1);
			aux.lleg.sum(t);
			trips.push_back(aux);
		}

		res=answer(trips,i);

		

		trips.clear();

	}


}