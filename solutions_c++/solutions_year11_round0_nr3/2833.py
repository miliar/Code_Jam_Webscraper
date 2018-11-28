#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <math.h>
#include <stdio.h>
using namespace std;
int power(int val,int muti){
	int a=1;
	for(int i=0;i<muti;i++){
		a*=val;
	}
	return a;
}

int main(){
	//freopen("sample.in","r",stdin);
	//freopen("sample.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int Candies;
		cin>>Candies;
		vector<int> Candy;
		vector<int> bin;
		for(int i=0;i<Candies;i++){
			int c;
			cin>>c;
			Candy.push_back(c);
			bin.push_back(0);
		}
		
		int SeanPile=0;
		//binary traversal
		for(unsigned int i=1;i<power(2,Candies)-1;i++){
		    int comb = i;
			int p=0;
			while(comb){
				bin[p++] = comb%2;
				comb /=2;
			}
			int pile1=0,pile2=0;
			int pile1P=0,pile2P=0;
			for(int j=0;j<Candies;j++){
				if (bin[j]){
					pile1+=Candy[j];
					pile1P^=Candy[j];
				} else {
					pile2+=Candy[j];
					pile2P^=Candy[j];
				}
			}
			if (pile1P==pile2P){
				int thispile=max(pile1,pile2);
				if (thispile>SeanPile){
					SeanPile=thispile;
				}
			}
		}

		if (0==SeanPile){
			cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
		} else {
			cout<<"Case #"<<i+1<<": "<<SeanPile<<endl;
		}
		
	}
	
	
}