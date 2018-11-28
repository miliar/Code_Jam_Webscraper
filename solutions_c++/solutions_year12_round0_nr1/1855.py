#include<iostream>
#include<fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
		
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("output1.out","wt",stdout);
	int totalCases;
	scanf("%d",&totalCases);
	char normal[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char converted[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char newLine;
	scanf("%c",&newLine);
	for(int i=0;i<totalCases;i++)
	{
		//cout << "Case #" << (i+1) <<": ";
		printf("Case #%d: ",(i+1));
		char ch='0';		
		while(ch != '\n')
		{
			scanf("%c",&ch); 
			if(ch==' ') printf("%c",' ');

			else
			for(int j=0;j<=25;j++)
			{
				if(ch==normal[j])
				{
					printf("%c",converted[j]);
					break;
				}
			} 
		}
		printf("\n");
	}
}
