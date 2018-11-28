#include<map>
#include<cstdio>
#include<string>
#include<vector>

#define pb push_back

using namespace std;

int main(){
	string str,p;
	int T,sout,C,D,len;
	char in[110],out[1001];
	map<char,bool> dentro;
	map<string,string> comb;
	vector<char> oposto[26];

	scanf("%d",&T);
	//printf("%d",T);
	for(int i=0; i<T; i++){
		comb.clear();
		dentro.clear();
		for(int j=0; j<26; j++)
			oposto[j].clear();

		scanf("%d",&C);			//	Combinações
		//printf("Here\n");
		for(int j=0; j<C; j++){
			scanf("%s",in);
			p = "", p += in[2];
			str = "", str += in[0], str += in[1];
			comb[str] = string(p);
			str = "", str += in[1], str += in[0];
			comb[str] = string(p);
			//printf("\t\t%s %s\n",str.c_str(),p.c_str());
		}
		scanf("%d",&D);			//	Opostos
		//printf("Here\n");
		for(int j=0; j<D; j++){
			scanf("%s",in);
			oposto[(in[0]-'A')].pb(in[1]);
			oposto[(in[1]-'A')].pb(in[0]);
			//printf("\t\t\t%c %c\n",in[0],in[1]);
		}

		scanf("%d %s",&len,in);
		dentro[in[0]] = true;
		out[0] = in[0], sout = 1;
		for(int j=1; j<len; j++){
			if(sout>0){
				str = "", str += out[sout-1], str += in[j];
				if( (str = comb[str]) != "" ){
					dentro[out[sout-1]] = false;
					out[sout-1] = str[0];
					for(int k=0; k<sout; k++) dentro[out[k]] = true;
				}else{
					out[sout] = in[j];
					dentro[in[j]] = true;
					sout++;
					for(int k=0, pos=(in[j]-'A'); k<oposto[pos].size(); k++){
						//printf("\t%c\n",oposto[pos][k]);
						if( dentro[oposto[pos][k]] == true ){
							sout = 0;
							dentro.clear();
						}
					}
				}
			}else{
				dentro[in[j]] = true;
				out[0] = in[j], sout = 1;
			}
		}
		out[sout] = '\0';
		if(sout==0)
			printf("Case #%d: []\n",i+1);
		else	if(sout==1)
					printf("Case #%d: [%c]\n",i+1,out[0]);
				else{
					printf("Case #%d: [%c",i+1,out[0]);
					for(int j=1; j<sout; j++)
						printf(", %c",out[j]);
					printf("]\n");
				}
	}
	return 0;
}
