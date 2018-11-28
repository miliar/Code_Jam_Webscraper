#include <iostream>
#include <sstream>
using namespace std;
int main(int argc, char** argv)
{
	FILE* infile = fopen(argv[1], "r");
	FILE* outfile = fopen("A-small.out", "w");
	if(infile == NULL){
		//cout<< "fopen error"<< endl;
		return 1;
	}
	if(outfile == NULL){
		//cout<< "fopen error"<< endl;
		return 1;
	}
		
	int L=0, D=0, N=0;
	char *buf = (char*)malloc(500);
	memset(buf, 0, 500);
	if(fgets(buf, 300, infile) ==NULL){
		//cout<<"fgets error\n"<<endl;
	}
	//cout<<buf<<endl;
	stringstream  ss(stringstream::in | stringstream::out);
	ss << buf;
	ss >> L >> D >> N;
	char **words = new char*[D];
	for(int i=0; i<D; i++){
		words[i] = new char[L];
		memset(words[i], 0, L);
	}
	char ***pattern = new char**[N];
	for(int i=0; i<N; i++){
		pattern[i] = new char*[L];
		for(int j=0; j<L; j++){
			pattern[i][j] = new char[26];
			memset(pattern[i][j], 0, 26);
		}
	}
	for(int i=0; i<D; i++){
		fgets(words[i], L+2, infile);
		//fgets(words[i], L, infile);
		//cout<<words[i]<<endl;
	}
	//cout<<endl;
	for(int i=0; i< N; i++){
		memset(buf, 0, 500);
		fgets(buf, 500, infile);
		//int len = (int)strlen(buf)-1;
		int len = (int)strlen(buf)-1;
		int j=0;
			for(int k=0; k<len; k++){
				if(buf[k] == '('){
					while(buf[++k] != ')'){
						pattern[i][j][buf[k]-'a'] = 1;
						//cout<<i<<" "<<j<<" "<< buf[k]-'a' << "  "<<buf[k] <<endl;
					}
					j++;
				}else{
	
					pattern[i][j][buf[k]-'a'] = 1;
					
					//cout<<i<<" "<<j<<" "<< buf[k]-'a' << "  "<<buf[k] <<endl;
					j++;
				}
			}
	}
	int *res = new int[N];
	memset(res, 0, N * sizeof(int));
	for(int i=0; i<D; i++){
		for( int k=0; k<N; k++){
			int j = 0;
			for(; j<L; j++){
				if( pattern[k][j][words[i][j]-'a'] != 1)
					break;
			}
			if(j >= L)
				res[k]++;
		}
	}
	char s[50];
	for(int i=1; i<=N; i++){
		//cout<< "Case #" << i << ": " << res[i-1] <<endl; 
		sprintf(s, "Case #%d: %d\n", i, res[i-1]);
		fputs(s, outfile);
	}
	delete[] words;
	delete[] pattern;
	delete[] res;
	fclose(infile);
	fclose(outfile);
	return 0;
}
