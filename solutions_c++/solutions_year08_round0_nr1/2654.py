#include <cstdio>
#include <fstream>
#include <string>
using namespace std;
char str[101][101];
char flag[101];

int IsValid(int s)
{
        int k = 0;
	for(int i = 1; i <= s; i++)
		if(!flag[i]) k++;
	return k;
}
int Solve(int s, char str1[101])
{
	int k = IsValid( s );
	for(int i = 1; i <= s; i++){
		if(strcmp(str[i], str1) == 0 && (k > 1 || (k == 1 && flag[i]))){if(k > 1) k--; flag[i] = 1;}
		else if(strcmp(str[i],str1) == 0 && k == 1 && !flag[i]){
			memset(flag, 0, sizeof(flag));
			flag[i] = 1;
			return 1;
		}
	}
	return 0;
}
int main()
{
	int n, s, q, ans;
	char str1[101];
	//str1 = new char[101];
	ifstream in("A-small-attempt1.in");
	ofstream out("b.out");
	in >> n;
	memset(flag, 0, sizeof(flag));
	for(int i = 0; i < n; i++){
		in >> s;
		ans = 0;
		in.getline(str[0], sizeof(str[0]));
		for(int j = 1; j <= s; j++){
			
			in.getline(str[j], sizeof(str[j]));
			
			//vst[str[j]]++;
		}
		in >> q;
		in.getline(str1,sizeof(str1));
		for(int k = 0; k < q; k++){
			
			in.getline(str1,sizeof(str1));
			if( Solve(s, str1)) ans++;
		}	
		out << "Case #" << i + 1 << ": " << ans <<endl;
		memset(flag, 0, sizeof(flag));
	}
	return 0;
}
