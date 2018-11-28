#include <iostream>
#include <map>
#include <vector>
using namespace std;

int tn;
string str;

int main(){
	int i,j;

     scanf("%d",&tn);
     for (int test = 1;test<=tn;test++){
		int base=2;
		map<char,int> m;
		bool nol = false;
		vector<int> hasil;
		
		cin >> str;

		m[str[0]]=1;
		hasil.push_back(1);
		for (i=1;i<str.length();i++){
			if (m.find(str[i])==m.end()){
				if (nol==false){
					nol=true;
					m[str[i]]=0;
				} else {
					m[str[i]]=base;
					base++;
				}
			}
			hasil.push_back(m[str[i]]);
		}
		
		//for (i=0;i<hasil.size();i++)
		  //   printf("%d\n",hasil[i]);
		
		long long res=0;
		long long multip=1;
		
		for (i=hasil.size()-1;i>=0;i--){
			res+=(long long)multip*(long long)hasil[i];
			multip*=(long long)base;
		}
		
		printf("Case #%d: ",test);
		cout << res << endl;
     }
     return 0;
}
