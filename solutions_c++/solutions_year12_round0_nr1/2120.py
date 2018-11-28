#include <iostream>

using namespace std;

int main()
{
	FILE* inFP = fopen("A-small-attempt0.in","rb");
	FILE* outFP = fopen("1.out","wb");
	char MAP[26] =
	{'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	int T;
	char c;
	fscanf(inFP,"%d",&T);
	fscanf(inFP,"%c",&c);
	for(int t=1;t<=T;t++)
	{
		fprintf(outFP,"Case #%d: ",t);
		do
		{
			c=EOF;
			fscanf(inFP,"%c",&c);

			if(c==' ')
				fprintf(outFP,"%c",c);
			else if(c>='a' && c<='z')
				fprintf(outFP,"%c",MAP[c-'a']);
			else
			{
				fprintf(outFP,"\n");
				break;
			}
		}while(c!=EOF);
	}


	fclose(inFP);
	fclose(outFP);
	return 0;
}