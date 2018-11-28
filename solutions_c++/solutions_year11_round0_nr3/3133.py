#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#define REP(i,t) for(i=0;i<t;i++)

using namespace std;

int pat(int x, int y){

int i;
int b = 2;
int sum = 0;
for(i = 0; x>0 || y>0; y = y>>1, x = x>>1, i++){
    sum+= abs(x%2 - y%2)*(pow(2,i));}
return sum;
}


int main(void){

int nCases, i,y,j, k;
int result;
int N,c[1000];
long long sb, s;
long long sba, sa;
long long x,xb;
int met;
int m[1000];

cin >> nCases;



REP(i,nCases){
  result = met= sb = s = sba = sa = 0;
  memset(m, 0, sizeof(int)*1000);
cin >> N;
REP(j,N){
cin >> c[j];
met+= c[j];
}
met = met/2;
//sort(c);

REP(j, N){

 memset(m, 0, sizeof(int)*1000);
 m[j] = 1;s=c[j];sa = c[j];
        REP(y,N){
 x = 0;xb=0;
            if(m[y]==0 && y>0){
                s+= c[y];
                sa = pat(c[y], sa);
                m[y] = 1;



                }

                REP(k,N){//cout << k <<"->" <<m[k]<<endl;
                if(m[k]==0){//cout << k << "##";
                x+= c[k];
                if(xb==0)
                    xb = c[k];
                else
                xb = pat(xb,c[k]);
                //cout << k;
                }
//cout << endl;
            }
           //cout << xb << " - " << x << "&" << s << " ¨  " << sa << endl;
            if(sa==xb && x>0 && s>0){//cout << xb << " - " << x << "&" << s << " ¨  " << sa << endl;
                if(x>s){
                    if(x>=result)result = x;}else{ if(s>=result)result = s;}

                    }

        }

        }






if(result == 0)
cout << "Case #" << i+1 << ": "<<"NO" << endl;
else
cout << "Case #" << i+1 << ": "<<result << endl;
}

}

