#include<iostream>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

long long int miPot(int b, int e){
    long long int res = 1;
    while(e){
        res *= b;
        e--;
    }
    return res;
}

vector<int> int2bin(long long int n){
    vector<int> res;
    if(n==0){
        res.push_back(0);
        return res;
    }
    while(n){
        res.push_back(n%2);
        n /= 2;
    }
    return res;
}

long long int bin2int(vector<int> v){
    long long int res = 0;
    for(int i=0;i<v.size();++i){
        res += v[i]*miPot(2,i);
    }
    return res;
}

long long int sumPat(long long int total, long long int act){
    long long int res=0;
    vector<int> sres;
    vector<int> tot = int2bin(total);
    vector<int> sact = int2bin(act);
    int s = max(tot.size(),sact.size());
    for(int i=0;i<s;++i){
        if(i<tot.size() && i<sact.size()){
            sres.push_back((tot[i]+sact[i])%2);
        } else{
            if(i<tot.size()){
                sres.push_back(tot[i]);
            } else{
                sres.push_back(sact[i]);
            }
        }
    }
    res = bin2int(sres);
    return res;
}

int main(){

	ifstream entrada("C-large.in");
	ofstream salida("C-large.out");

	int Casos;
	entrada >> Casos;
	for(int caso=1;caso<=Casos;++caso){
	    long long int res = 0;
        int N;
        entrada >> N;
        vector<long long int> val;
        bool posible = false;
        long long int total = 0;
        for(int i=0;i<N;++i){
            long long int aux;
            entrada >> aux;
            val.push_back(aux);
            total = sumPat(total, aux);
        }
        if(total == 0){
            posible = true;
        }
        if(posible){
            sort(val.begin(),val.end());
            for(int i=1;i<N;++i){
                res += val[i];
            }
        }


        if(posible){
            salida << "Case #" << caso << ": " << res << endl;
        } else{
            salida << "Case #" << caso << ": NO" << endl;
        }
	}
	return 0;
}
