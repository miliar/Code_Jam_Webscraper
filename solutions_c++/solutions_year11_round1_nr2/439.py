//B

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	//vars
	int T,t;
	int n,m,a,b,c,d,r,ln;
	int bestI,bestN,curN;
	char lst[30];
	static int len[10001];
	static char dict[10001][12];
	static int let[10001][30];
	static int rem[10001];
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			memset(let,0,sizeof(let));
			//input
			scanf("%d %d\n",&n,&m);
				for (a=0; a<n; a++)
				{
					scanf("%s\n",&dict[a]);
					len[a]=strlen(dict[a]);
						for (b=0; b<len[a]; b++)
							let[a][dict[a][b]-'a']++;
				}
			//go through each list
			printf("Case #%d:",t);
				while (m--)
				{
					//input
					scanf("%s\n",&lst);
					//try each word
					bestN=-1;
						for (a=0; a<n; a++)
						{
							//init
							ln=len[a];
							curN=0;
							r=0;
								for (b=0; b<n; b++)
									if (ln==len[b])
										rem[r++]=b;
							//simulate
								for (b=0; b<26; b++)
								{
									//is this letter possible?
									for (c=0; c<r; c++)
										if (let[rem[c]][lst[b]-'a'])
											goto good;
									//possible
									if (false)
									{
good:
										//wrong move
										if (!let[a][lst[b]-'a'])
										{
											curN++;
											//eliminate words
												for (d=r-1; d>=0; d--)
													if (let[rem[d]][lst[b]-'a'])
													{
															if (d<r-1)
																rem[d]=rem[r-1];
														r--;
													}
										}
										else
										{
											//use this letter, eliminate words
												for (c=0; c<ln; c++)
													for (d=r-1; d>=0; d--)
														if (bool(dict[rem[d]][c]==lst[b])!=bool(dict[a][c]==lst[b]))
														{
																if (d<r-1)
																	rem[d]=rem[r-1];
															r--;
														}
										}
										//only 1 left?
										if (r==1)
											break;
									}
								}
							//new best?
								if (curN>bestN)
								{
									bestN=curN;
									bestI=a;
								}
						}
					//output
					printf(" %s",dict[bestI]);
				}
			printf("\n");
		}
	return(0);
}