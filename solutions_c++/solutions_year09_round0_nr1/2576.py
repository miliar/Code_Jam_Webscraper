#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <queue>

using namespace std;

int L, D, N;

map<string,int> dict;
char word[20];
char temp[500];
int branches;
char msg[30][35];
bool onBranch;
int caseNum;
int index;
map<string,int> visited;

struct state {
	int branch;
	char word[20];
	
	state(int branch=0,char word[20]) {
		strcpy(this->word, word);
		this->branch = branch;
	}
};

queue<state> next;

void search() {
	while(!next.empty()) next.pop();
	
	int answer = 0;
	visited.clear();
	
	next.push( state(0,"") );
	
	while(!next.empty()) {
		state now = next.front();
		next.pop();
		
		if (now.branch==L) {
			answer++;
			//printf("answer: %s\n", now.word);
		}
		else {	
			for(int i = 0; msg[now.branch][i]; i++) {
				memset(temp,0,sizeof(temp));
				strcpy(temp, now.word);
				temp[now.branch] = msg[now.branch][i];
				
				if (dict[temp]) {
					if (!visited[temp]) {
						next.push( state(now.branch+1, temp) );
						visited[temp] = 1;
					}
				}
			}
		}
	}
	
	caseNum++;
	printf("Case #%d: %d\n",caseNum,answer);
}


bool read() {
	return scanf("%d %d %d",&L,&D,&N)==3;
}

void process() {
	dict.clear();
	gets(temp);
	
	for (int i = 0; i < D; i++) {
		scanf("%s",word);
		//printf("read: %s\n", word);
		memset(temp,0,sizeof(temp));
		for (int j = 0; word[j]; j++) {
			temp[j] = word[j];
			dict[temp]=1;
		}
	}
	
	
	for (int i = 0; i < N; i++) {
		scanf("%s",temp);
		memset(msg,0,sizeof(msg));
		onBranch = false;
		branches = 0;
		
		index = 0;
		
		for(int j = 0; temp[j]; j++) {
			//printf("Reading '%c'...\n",temp[j]);
			if (temp[j]=='(') {
				onBranch = true;
			}
			else if (temp[j]==')') {
				//printf("branch (%d): %s\n",index, msg[branches]);
				
				branches++;
				index=0;
				onBranch = false;
			}
			else {
				if (onBranch) {
					msg[branches][index] = temp[j];
					index++;
				}
				else {
					
					msg[branches][index] = temp[j];
					//printf("branch (%d): %s\n",index, msg[i]);
					
					branches++;
					index=0;
				}
			}
		}
		
		search();
		
	}
}



int main() {
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	
	caseNum=0;
	
	while (read()) process();
	
	return 0;
}
