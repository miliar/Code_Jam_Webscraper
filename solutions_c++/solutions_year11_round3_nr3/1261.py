#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main(int argc, char ** argv){

int  T, k;
unsigned long long i,j, L, H, aux, N;

cin >> T;

vector <unsigned long long> played;
vector <unsigned long long> tested;

bool test;

for(k=1;k<=T;k++){
cout << "Case #" << k <<": ";
cin >> N >> L >> H;

played.clear();

for(i=0;i<N;i++){
cin >> aux;
played.push_back(aux);
}

tested.clear();


for(i=L;i<=H;i++){
test = true;

/*for(j=0;j<tested.size();j++){
	if (i%tested[j] == 0) {test = false; break;}
}*/


//if (test == true)
{
for(j=0;j<played.size();j++)
	{
		if(played[j] >= i){ 
			if(played[j] % i != 0) {tested.push_back(i); break; }
			}
		else if (i%played[j] != 0) {tested.push_back(i); break; }
	}

if(j>=played.size())
	{cout << i << endl; break;}
}
}

if (i>H) cout << "NO" << endl;

}

return 0;
}
