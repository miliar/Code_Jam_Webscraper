#include <stdio.h>
#include <string.h>
#include <malloc.h>

// ���丮�� �����Ϸ���
// base���� ����°� �����Ͱ���.

typedef struct dirtree {
	char name[256];
	dirtree *child[100];
} dirtree;

dirtree *origin[100];

int create_directory(const char *d)
{
	//�ٷ�� ���ϰ� �ϱ� ���ؼ�, ���� /�� �����Ѵ�.
	char *orgdir=(char *)malloc(strlen(d)),*tmp;
	char *orgdir2=orgdir;
	dirtree **p;
	int i,j,k=0,l=0;
	strcpy(orgdir,d+1);

	// ����, ���ϴ� ���丮�� ���� ������ ��� �˻��Ѵ�.
	// �ٵ� �˻��ϴ� ����� �̷��ϴ�.
	// ������ p�� ���, �ش� ������ �´� name�� �ֳ� �˻��Ѵ�.
	// ������ �ű⼭���� �ٽ� �˻��Ѵ�.
	// ���ٸ�, ��� ���� ����⸦ �ݺ��Ѵ�.

	p=origin;

	while (!l)
	{
		for (i=0; orgdir[i] != '/' && orgdir[i]; i++);
		// ���� orgdir[i]�� '/'�̴�.

		if (orgdir[i]==0) l=1;
		orgdir[i]=0;

		for (j=0; p[j]; j++)
		{
			if (strcmp(p[j]->name, orgdir) == 0) // name �߰�����!
			{
				orgdir=orgdir+i+1;
				p=p[j]->child;
				goto loopstart;
			}
		}

		if (p[j] == 0) // name �߰� ������. �̶����� ��� ����������.
		{
			// ����� �˰����� ���� �̷��Ͱ���.
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