#include <stdio.h>
#include <string.h>
#include <malloc.h>

// 디렉토리를 구현하려면
// base부터 만드는게 좋을것같다.

typedef struct dirtree {
	char name[256];
	dirtree *child[100];
} dirtree;

dirtree *origin[100];

int create_directory(const char *d)
{
	//다루기 편하게 하기 위해서, 앞의 /는 제외한다.
	char *orgdir=(char *)malloc(strlen(d)),*tmp;
	char *orgdir2=orgdir;
	dirtree **p;
	int i,j,k=0,l=0;
	strcpy(orgdir,d+1);

	// 이제, 원하는 디렉토리가 나올 때까지 계속 검색한다.
	// 근데 검색하는 방법은 이러하다.
	// 포인터 p를 잡고, 해당 레벨에 맞는 name이 있나 검색한다.
	// 있으면 거기서부터 다시 검색한다.
	// 없다면, 계속 새로 만들기를 반복한다.

	p=origin;

	while (!l)
	{
		for (i=0; orgdir[i] != '/' && orgdir[i]; i++);
		// 이제 orgdir[i]는 '/'이다.

		if (orgdir[i]==0) l=1;
		orgdir[i]=0;

		for (j=0; p[j]; j++)
		{
			if (strcmp(p[j]->name, orgdir) == 0) // name 발견했음!
			{
				orgdir=orgdir+i+1;
				p=p[j]->child;
				goto loopstart;
			}
		}

		if (p[j] == 0) // name 발견 못했음. 이때부터 계속 만들어나가야함.
		{
			// 만드는 알고리즘은 대충 이럴것같다.
			for (;;)
			{
				p[j]=(dirtree *)calloc(1,sizeof(dirtree));
				strcpy(p[j]->name,orgdir);
				orgdir=orgdir+i+1;
				p=p[j]->child;
				j=0;

				k++;

				if (l) break;

				for (i=0; orgdir[i] != '/' && orgdir[i]; i++);
				if (orgdir[i]==0) l=1;
				orgdir[i]=0;
			};
		}

		loopstart:;
	}
	free(orgdir2);

	return k;
}

void freemem()
{
	memset(origin,0,sizeof(origin));
}

int main()
{
	FILE* fp=fopen("A-small-attempt0.in","r"),*fp2=fopen("output.out","w");
	int t,n,m,i,j,k;
	char text[256];
	fscanf(fp,"%d",&t);
	for (i=1; i<=t; i++)
	{
		k=0;
		fscanf(fp,"%d%d",&n,&m);
		for (j=0; j<n; j++)
		{
			fscanf(fp,"%s",text);
			create_directory(text);
		}

		for (j=0; j<m; j++)
		{
			fscanf(fp,"%s",text);
			k += create_directory(text);
		}

		fprintf(fp2,"Case #%d: %d\n",i,k);

		freemem();
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}