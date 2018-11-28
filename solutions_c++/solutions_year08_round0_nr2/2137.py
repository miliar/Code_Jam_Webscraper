#include<iostream>
#include<string>
#include<list>
#include<queue>

using namespace std;
/*
   class t{
   int depT, arrT;
   bool s; 
   };

   Compare& x{
   arrT
   }*/
int main(){
	int cases, turn, na, nb;
	string aX, dX;
	cin >> cases;
	for(int n=0; n<cases; n++){
		cin >> turn >> na >> nb;		
		int aDep[na], bArr[nb], aArr[na], bDep[nb];//, a[na], b[nb];
		int aD[na], aA[na], bD[nb], bA[nb];
		//		priority_queue <t> aDep(x), aArr(x), bDep(x), bArr(x);
		for(int j=0; j<na; j++){
			cin >> dX >> aX;
			aDep[j] = (atoi(dX.substr(0,2).c_str())*60 + atoi(dX.substr(3,2).c_str()));
			aArr[j] = (atoi(aX.substr(0,2).c_str())*60 + atoi(aX.substr(3,2).c_str()) + turn);
		}
		for(int j=0; j<nb; j++){
			cin >> dX >> aX;
			bDep[j] = (atoi(dX.substr(0,2).c_str())*60 + atoi(dX.substr(3,2).c_str()));
			bArr[j] = (atoi(aX.substr(0,2).c_str())*60 + atoi(aX.substr(3,2).c_str()) + turn);
		}
//		cout << "input complete\n";
		int Aa=0, Da=0, Ab=0, Db=0, a=0, d=0, b=0, c=0;
		bool aa[na], ab[na], ba[nb], bb[nb];	
		for(int i=0; i<na; i++){
			if(aArr[i] < aArr[Aa]) Aa = i;
			if(aDep[i] < aDep[Da]) Da = i;
			if(aArr[i] > aArr[a]) a = i;
			if(aDep[i] > aDep[d]) d = i;
			aa[i] = false;
			ab[i] = false;
		}
		for(int i=0; i<nb; i++){
			if(bArr[i] < bArr[Ab]) Ab = i;
			if(bDep[i] < bDep[Db]) Db = i;
			if(bArr[i] > bArr[b]) b = i;
			if(bDep[i] > bDep[c]) c = i;
			ba[i] = false;
			bb[i] = false;
		}
		aA[0] = Aa;
		aD[0] = Da;
		bA[0] = Ab;
		bD[0] = Db;
		aa[Aa] = true;
		ab[Da] = true;
		ba[Ab] = true;
		bb[Db] = true;
//		cout <<"reached\t"<<aD[0]<<"\t"<<aA[0]<<"\t"<<bD[0]<<"\t"<<bA[0]<<d<<"\t"<<c<<"\t"<<b<<"\t"<<a<<"\n";
		for(int i=1; i<na; i++){
			int ka = a, kd = d;
			for(int j=0; j<na; j++){
				if(!aa[j] && aArr[j] < aArr[ka] && aArr[j] >= aArr[aA[i-1]]) ka = j;
				if(!ab[j] && aDep[j] < aDep[kd] && aDep[j] >= aDep[aD[i-1]]) kd = j;
			}
			aA[i] = ka;
			aD[i] = kd;
			aa[ka] = true;
			ab[kd] = true;
		//	cin >> aD[i] >> aA[i];
		}
		for(int i=1; i<nb; i++){
			int ka = b, kd = c;
			for(int j=0; j<nb; j++){
				if(!ba[j] && bArr[j] < bArr[ka] && bArr[j] >= bArr[bA[i-1]]) ka = j;
				if(!bb[j] && bDep[j] < bDep[kd] && bDep[j] >= bDep[bD[i-1]]) kd = j;
			}
			ba[ka] = true;
			bb[kd] = true;
			bA[i] = ka;
			bD[i] = kd;/**/
//			cin >> bD[i] >> bA[i];
		}
		int sA= 0, sB =0, eA = 0, eB = 0, t=0;
		a = -1, b = -1, c = -1, d = -1;
/*		for(int i=0; i<na; i++){
			cout << aD[i] <<"\t"<<aA[i]<<"\n";
		}
		for(int i=0; i<nb; i++){
			cout << bD[i] <<"\t"<<bA[i]<<"\n";
		}
		cout <<"before loop\n";
*/		while(a < na-1 || b < nb-1 || c < nb-1 || d < na-1){
			int ta, tb, tc, td;
			if(a < (na-1)) ta = aArr[aA[a+1]];
			else ta = 48*60;
			if(b < (nb - 1)) tb = bArr[bA[b+1]];
			else tb = 48*60;
			if(c < (nb - 1)) tc = bDep[bD[c+1]];
			else tc = 48*60;
			if(d < (na - 1)) td = aDep[aD[d+1]];
			else td = 48*60;
//			int ta = aArr[aA[a+1]], tb = bArr[bA[b+1]], tc = bDep[bD[c+1]], td = aDep[aD[d+1]];
			if(ta <= tb && ta <= tc && ta <= td){
//				cout << "in a\n";
				eB++;
				a++;
				t = ta;
			}
			else if(tb <= td && tb <= tc){
//				cout << "in b\n";
				eA++;
				b++;
				t = tb;
			}
			else if(td <= tc){
//				cout << "in d\n";
				if(eA>0){
					eA--;
					d++;
				}
				else{
					sA++;
//					cout << "sA ="<<sA<<endl;
					d++;
				}
				t = td;
			}
			else{
//				cout << "in c\n";
				if(eB > 0) eB--;
				else {
					sB++;
//					cout << "sB = "<<sB<<endl;
				}
				c++;
				t = tc;
			}
		}
		cout << "Case #"<<n+1<<": "<<sA<<" "<<sB<<endl;

	}
	return 0;
}
