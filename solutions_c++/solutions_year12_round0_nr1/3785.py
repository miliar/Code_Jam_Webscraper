#include <cstdio>
#include <cstring>

const int MAXLEN=100;
char inv_map[26];
char str[2][MAXLEN+11];
int main()
{
	/*gets(str[0]);
	printf("%d\n", strlen(str[0]));*/
	int T, t, i, pref;
	FILE *fi, *fo;
	memset(inv_map, -1, sizeof(inv_map));
	fi=fopen("example_input.txt", "r");
	fo=fopen("example_output.txt", "r");
	fscanf(fi, "%d", &T);
	fgetc(fi);
	pref=9;
	for(t=0; t<T; ++t)
	{
		fgets(str[0], MAXLEN+2, fi);
		fgets(str[1], MAXLEN+2+pref, fo);
		for(i=0; str[0][i]!='\n'; ++i)
			if(str[0][i]!=' ')
				inv_map[str[0][i]-'a']=str[1][i+pref];
	}
	inv_map['q'-'a']='z';
	inv_map['z'-'a']='q';
	fclose(fi);
	fclose(fo);
	
	/*for(i=0; i<26; ++i)
		if(inv_map[i]>=0)
			printf("%c -- %c\n", 'a'+i, inv_map[i]);
		else
			printf("%c -- -1\n", 'a'+i);*/
	//fi=fopen("input.txt", "r");
	fi=fopen("A-small-attempt1.in", "r");
	fo=fopen("output.txt", "w");
	fscanf(fi, "%d", &T);
	fgetc(fi);
	for(t=1; t<=T; ++t)
	{
		fgets(str[0], MAXLEN+2, fi);
		sprintf(str[1], "Case #%d: ", t);
		pref=strlen(str[1]);
		for(i=0; str[0][i]!='\n'; ++i)
			str[1][i+pref]=(str[0][i]==' ' ? ' ' : inv_map[str[0][i]-'a']);
		str[1][i+pref]='\n';
		str[1][i+pref+1]='\0';
		fputs(str[1], fo);
	}
	return 0;
}
