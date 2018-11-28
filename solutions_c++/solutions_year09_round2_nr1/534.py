#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX_IN = 10000;
char IN[MAX_IN];

const int MAX_ANYM = 100;
const int MAX_TOKEN = 30;
char anym_names[MAX_ANYM][MAX_TOKEN];
int anym_feat_count[MAX_ANYM];
char anym_feat[MAX_ANYM][100][MAX_TOKEN];

struct node_s{
	double p;
	char name[MAX_TOKEN];
	node_s * first;
	node_s * sec;
};

char*p;
char token[MAX_TOKEN];

void nextToken(){
	if(p)
		sscanf(p,"%s",token);
	else
		token[0]=0;
	p = strtok(NULL," ");
}

node_s * read(){
	node_s * node = new node_s;
	nextToken();
	char ver[MAX_TOKEN];
	while(token[0] == ')')
		nextToken();
	if(strlen(token) == 1){
		if(token[0] != '('){
			cout << "token[0] != (";
			exit(1);
		}
		nextToken();
		strcpy(ver,token);
	}
	else{
		strcpy(ver,&token[1]);
		
	}

	//cout << "ver " << ver << endl;

	bool end = false;
	if(ver[strlen(ver)-1] == ')'){
		end = true;
		ver[strlen(ver)-1] = 0;
	}

	node->p = atof(ver);

	if(!end){
		nextToken();
		if(token[0] == ')')
			end = true;
	}

	node->name[0]=0;
	node->first=NULL;
	node->sec=NULL;

	if(!end){
		//nextToken();
		strcpy(node->name,token);
		node->first = read();
		node->sec = read();
	}

			
	//cout << node->name << ' ' << node->p << endl;
	return node;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _;
	cin >> _;

	for(int __=0; __<_; ++__){
		int L;
		cin >> L;
		ZER(IN);
		char buf[100];
		cin.getline(buf,sizeof(buf));
		for(int i=0; i<L; ++i){
			cin.getline(buf,sizeof(buf));
			strcat(IN,buf);
			strcat(IN," ");
		}
		//cout << L << ' ' << IN <<endl;
		p = strtok(IN," ");
		node_s * root = read();
		//do{
		//	nextToken();
		//	if(strlen(token)){
		//		cout << token << endl;
		//	}
		//}while(strlen(token));




		int n;
		cin >> n;
		for(int i=0; i<n; ++i){
			cin >> anym_names[i];
			cin >> anym_feat_count[i];
			for(int j=0; j<anym_feat_count[i]; ++j){
				cin >> anym_feat[i][j];
			}
		}


		//for(int i=0; i<n; ++i){
		//	cout << anym_names[i] << ' ';
		//	for(int j=0; j<anym_feat_count[i]; ++j){
		//		cout << anym_feat[i][j] << ' ';
		//	}
		//	cout << endl;
		//}

		printf("Case #%d:\n",__+1);
		//cout << "Case #" << __+1 << ": " <<endl;

		for(int i=0; i<n; ++i){
			double p = 1;
			node_s * node = root;
			while(node){
				p *= node->p;
				int j;
				for(j=0; j<anym_feat_count[i]; ++j){
					if( strcmp(anym_feat[i][j],node->name) == 0)
						break;
				}
				if(j<anym_feat_count[i])
					node = node->first;
				else
					node = node->sec;
			}
			printf("%.6lf\n",p);
			//cout << p << endl;
		}
		
		
	}
	return 0;
}