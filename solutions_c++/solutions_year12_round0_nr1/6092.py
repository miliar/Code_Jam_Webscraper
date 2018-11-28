#include <stdio.h>

int main()
{
char ch,tmp;
int n;
bool flag=true;
FILE *f,*fo;
f = fopen("small.in","r");
fo = fopen("small.out","w");
fscanf(f,"%d",&n);
fscanf(f,"%c",&tmp);
for(int i=1;i<=n;i++)
{
	fprintf(fo,"Case #%d: ",i);
	ch = '\0';
	
	while(ch != '\n' && !feof(f))
	{
		fscanf(f,"%c",&ch);
	switch(ch)
	{
	case 'a':
		fprintf(fo,"y");
		break;
	case 'b':
		fprintf(fo,"h");
		break;
	case 'c':
		fprintf(fo,"e");
		break;
	case 'd':
		fprintf(fo,"s");
		break;
	case 'e':
		fprintf(fo,"o");
		break;
	case 'f':
		fprintf(fo,"c");
		break;
	case 'g':
		fprintf(fo,"v");
		break;
	
	case 'h':
		fprintf(fo,"x");
		break;
	
	case 'i':
		fprintf(fo,"d");
		break;
	
	case 'j':
		fprintf(fo,"u");
		break;
	
	case 'k':
		fprintf(fo,"i");
		break;
	
	case 'l':
		fprintf(fo,"g");
		break;
	
	
	case 'm':
		fprintf(fo,"l");
		break;
	
	case 'n':
		fprintf(fo,"b");
		break;
	
	case 'o':
		fprintf(fo,"k");
		break;
	
	case 'p':
		fprintf(fo,"r");
		break;
	
	case 'q':
		fprintf(fo,"z");
		break;
	
	case 'r':
		fprintf(fo,"t");
		break;
	
	case 's':
		fprintf(fo,"n");
		break;
	
	case 't':
		fprintf(fo,"w");
		break;
	
	case 'u':
		fprintf(fo,"j");
		break;
	
	case 'v':
		fprintf(fo,"p");
		break;
	
	case 'w':
		fprintf(fo,"f");
		break;
	
	case 'x':
		fprintf(fo,"m");
		break;
	
	case 'y':
		fprintf(fo,"a");
		break;
	
	case 'z':
		fprintf(fo,"q");
		break;
	
	case ' ':
		fprintf(fo," ");
		break;
	}
}
fprintf(fo,"\n");
}
fclose(f);
fclose(fo);
}