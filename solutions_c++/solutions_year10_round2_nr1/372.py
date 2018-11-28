#include<cstdio>
#include<vector>

using namespace std;

struct Node;

struct Tree
{
	Node * root;
};

struct Node
{
	vector<Node*> ch;
	char name[105];
	Node* par;
};

int main()
{
	int T,N,M;
	char str[105];
	scanf("%d\n",&T);
	for(int ii = 1;ii <= T;++ii)
	{
		Tree* T = (Tree*)malloc(sizeof(Tree));
		T->root = (Node*)malloc(sizeof(Node));

		strcpy(T->root->name,"/");

		scanf("%d %d\n",&N,&M);
		for(int i = 0;i < N;++i)
		{
			scanf("%s\n",str);
			Node* temp = T->root;

			char * pch;
			pch = strtok(str,"/");
			while (pch != NULL)
			{
//				printf ("%s\n",pch);
				Node* ptr = NULL;
				for(int i = 0;i < temp->ch.size();++i) if(strcmp(pch,temp->ch[i]->name) == 0) ptr = temp->ch[i];

				if(ptr == NULL)
				{
					ptr = (Node*)malloc(sizeof(Node));
					strcpy(ptr->name,pch);
					temp->ch.push_back(ptr);
				}
				temp = ptr;
				pch = strtok (NULL, "/");
			}
		}

		int cmd = 0;
		for(int i = 0;i < M;++i)
		{
			scanf("%s\n",str);
			Node* temp = T->root;

			char * pch;
			pch = strtok(str,"/");
			while (pch != NULL)
			{
//				printf ("%s\n",pch);
				
				Node* ptr = NULL;
				for(int i = 0;i < temp->ch.size();++i)
					if(strcmp(pch,temp->ch[i]->name) == 0) ptr = temp->ch[i];

				if(ptr == NULL)
				{
					ptr = (Node*)malloc(sizeof(Node));
					strcpy(ptr->name,pch);
					temp->ch.push_back(ptr);
					cmd++;
				}
				temp = ptr;
				pch = strtok (NULL, "/");
			}
		}

		printf("Case #%d: %d\n",ii,cmd);
	}
	return 0;
}
