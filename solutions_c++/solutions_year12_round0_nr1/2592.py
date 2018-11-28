#include<stdio.h>
#include<string.h>

char translations[26]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'q'};

char input1[]="y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

char trans1[]="a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char getTrans(char character)
{
	if(character < 'a' || character > 'z')
		return character;
	if(translations[character-'a'] != 0)
		return translations[character-'a'];
	else 
		return '?';
}

void setTrans(char character, char translation)
{
	if(translations[character-'a'] == 0)
		translations[character-'a']=translation;
}

int main()
{
	int h, count=1, T;
	char text[128];

	//Base translation	
	for(h=0; h<strlen(input1); h++)
		if(input1[h]<='z' && input1[h]>='a')
			setTrans(input1[h], trans1[h]);

	FILE *f=fopen("input1.txt", "r");
	FILE *f2=fopen("output1.txt", "w");

	fscanf(f, "%d\n", &T);

	while(count <= T)
	{
		fgets(text, 120, f);
		
		for(h=0; text[h] != '\0'; h++)
			text[h]=getTrans(text[h]);

		fprintf(f2, "Case #%d: %s", count, text);

		count++;
	}

	fclose(f);
	fclose(f2);
}
