#include <iostream>
#include <queue>

using namespace std;


int main() {
	printf("Program start.\n");
	if(freopen("A-small-practice.in", "r", stdin)){
		freopen("A-small-practice.out","w",stdout);
	}else{
		printf("file not found.\n");
		return 0;
	}

//	if(freopen("A-large-practice.in", "r", stdin)){
//		freopen("A-large-practice.out","w",stdout);
//	}else{
//		printf("file not found.\n");
//		return 0;
//	}

	int TestCases;
	scanf("%d", &TestCases);

	for(int caseID=1;caseID<=TestCases;caseID++){
		printf("Case #%d: ", caseID);
		int rides, capa, groups;
		scanf("%d", &rides);
		scanf("%d", &capa);
		scanf("%d", &groups);
		//queue
		queue<int> q,w;
		int p;
		for(int i=0;i<groups;i++){
			scanf("%d", &p);
			q.push(p);
		}

		//ride
		int result=0;
		for(int i=0;i<rides;i++){
			int c=0;
			while((capa-c)>=q.front()&&!q.empty()){
				c+=q.front();
				w.push(q.front());
				q.pop();
			}
			result+=c;
			while(!w.empty()){
				q.push(w.front());
				w.pop();
			}
		}

		printf("%d", result);
		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);
	printf("Program finish.\n");
	return 0;
}
