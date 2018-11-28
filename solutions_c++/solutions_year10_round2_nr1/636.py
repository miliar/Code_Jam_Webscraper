#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 1000;


struct Node
{
	string s;
	Node *son[MAXN];
	int sonnum;

	Node()
	{
		s = "";
		sonnum = 0;
	}

	Node(string str)
	{
		s = str;
		sonnum = 0;
	}
};

Node *cur;
int ct = 0;

void insert(string s)
{
	bool find = false;
	for (int i=0; i<cur->sonnum; i++)
	{
		if (cur->son[i]->s == s)
		{
			find = true;
			cur = cur->son[i];
			break;
		}
	}

	if (!find)
	{
		Node * t = new Node(s);
		cur->son[cur->sonnum++] = t;
		cur = t;
	}
}



void query(string s)
{
	bool find = false;
	for (int i=0; i<cur->sonnum; i++)
	{
		if (cur->son[i]->s == s)
		{
			find = true;
			cur = cur->son[i];
			break;
		}
	}

	if (!find)
	{
		ct++;
		Node * t = new Node(s);
		cur->son[cur->sonnum++] = t;
		cur = t;
	}
}

int main()
{
    
    int cas;
    int n,m;
	int i,j,k;
	char temp[2];
	temp[1] = '\0';
	string s;


	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

    scanf("%d",&cas);
	int num = 1;
    
    while (cas--)
    {
          scanf("%d%d\n",&n,&m);

		  Node *head = new Node();

          ct = 0;
		  
          for (i=0; i<n; i++)
          {
              getchar();
			  
	
			  cur = head;
			  while (1)
			  {
				  s = "";
				  while (1)
				  {
					temp[0] = getchar();
					if (temp[0] == '/' || temp[0] == '\n') break;
					s = s + string(temp);
				  }

				  insert(s);

				  


				  if (temp[0] == '\n') break;
			  }

          }


          for (i=0; i<m; i++)
          {
              getchar();
		  cur = head;			  
			  int l = 0;

			  while (1)
			  {
				  s = "";
				  while (1)
				  {
					temp[0] = getchar();
					if (temp[0] == '/' || temp[0] == '\n') break;
					s = s + string(temp);
				  }

				  query(s);

				  


				  if (temp[0] == '\n') break;
				  l++;
			  }

          }
		
		  printf("Case #%d: %d\n",num++,ct);

          
    }      
    return 0;
}
