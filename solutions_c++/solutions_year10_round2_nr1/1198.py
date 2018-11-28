#include<stdio.h>
#include<string>
#include<vector>

using namespace std;

vector<string> ex;
int cnt;

int solve(string child){
	if(child == "") return 0;
	for(int i = 0; i < ex.size(); i++){
		//printf("%s\n", ex[i].c_str());
		if(child ==  ex[i]) return 0;
	}
	ex.push_back(child);
	int off = child.rfind("/");
	//printf("%s\n", child.c_str());
	//printf("%s\n", child.substr(0, off).c_str());
	return 1 + solve(child.substr(0, off));
}

void process(vector<string> exist, vector<string> nw, int N, int M){
//	for(int i = 0; i < N; i++)
//		printf("%s\n", exist[i].c_str());
//	for(int i = 0; i < M; i++)
//		printf("%s\n", nw[i].c_str());
	ex = exist;
	int ans = 0;
	for(int i = 0; i < M; i++){		
		ans += solve(nw[i]);
	}
	printf("Case #%d: %d\n", ++cnt, ans);
}

int main(){
	cnt = 0;
	FILE* pFile;
	char buffer [150];
	int T = 0;
	pFile = fopen ("A-large.in" , "r");
	fscanf(pFile, "%d\n", &T);
	
	for(int i = 0; i < T; i++){
		int N = 0, M = 0;
		fscanf(pFile, "%d %d\n", &N, &M);
		//printf("%d %d\n", N, M);
		vector<string> exist;
		for(int j = 0; j < N; j++){
			fgets(buffer, 150, pFile);
			string t;
			for(int i = 0; buffer[i] != '\n'; i++){
				t += buffer[i];
			}
			exist.push_back(t);
		}
		vector<string> nw;
		for(int j = 0; j < M; j++){
			fgets(buffer, 150, pFile);
			string t;
			for(int i = 0; buffer[i] != '\n'; i++){
				t += buffer[i];
			}
			nw.push_back(t);
		}
		process(exist, nw, N, M);
	}	
	fclose(pFile);
	getchar();
	return 0;
}
