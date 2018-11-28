#include<stdio.h>
#include<malloc.h>
#include<string.h>

typedef struct nn{
	char str[200];
	struct nn * childs[200];
	int no_childs;
}node ; 

int length_string ; 
int answer;

node * insert(node * parent , char * str , int index , int flag)
{
	if(index >= length_string)
		return parent;
	char p_dir[200];
	int i=index;
	int j=0;
	while(str[i] != '/' && str[i]!='\0')
	{
		p_dir[j++]=str[i];
		i++;
	}

	int check =0 ; 
	if(str[i] == '\0')
		check =1;

	i++;
	p_dir[j]='\0';
	for(j=0 ; j < parent->no_childs ; j++)
	{
		if(strcmp(p_dir, parent->childs[j]->str)==0)
		{
			parent->childs[j] = insert(parent->childs[j] , str , i , flag);
			return parent;
		}
	}

	if(j == parent->no_childs)
	{
		node * children;
		children = (node *) malloc(sizeof(node));
		
		parent->childs[parent->no_childs]=children;
		parent->childs[parent->no_childs]->no_childs =0 ;
		strcpy(parent->childs[parent->no_childs]->str,p_dir);
		parent->no_childs ++;
		insert(parent->childs[parent->no_childs-1], str , i , flag);
		if(flag == 1)
			answer ++ ; 
		return parent;
	}
	return parent;

}

int main(){
	char str[200];
		int N , M;  // N : already created
	int tc;
	scanf("%d",&tc);
	int i;
	for(i=1 ; i<=tc ; i++)
	{
		node * root;
		root = (node *) malloc(sizeof(node));
		root->no_childs =0 ;

		answer = 0;
		scanf("%d%d",&N,&M);
		for(int j=0 ; j<N ; j++)
		{
			scanf("%s",str);
			length_string = strlen(str);
			root = insert(root , str , 1 ,0);
		}
		for(int j=0 ; j<M ; j++)
		{
			scanf("%s",str);
			length_string = strlen(str);
			root = insert(root , str , 1 ,1);
		}

	printf("Case #%d: %d\n",i,answer);
	}
	

	return 0;
}
