 #include<iostream>
 #include<CString> 
 using namespace std;
 string map[4];
 void Solve(int n)
 {
// 	for (int i=0;i<4;++i)
 //	cout<<map[i]<<endl;
 	printf("Case #%d: ",n);
 	string Role="XO";
 	for (int z=0;z<2;++z)
 	{
 		for (int i=0;i<4;++i)
 		{
 			int cnt=0;
 			for (int j=0;j<4;++j)
 			if (map[i][j]==Role[z] || map[i][j] == 'T') cnt++;
 			if (cnt == 4) 
			{
			 cout<<Role[z];
			 printf(" won\n");
			 return ;
			}
			cnt=0;
 			for (int j=0;j<4;++j)
 			if (map[j][i]==Role[z] || map[j][i] == 'T') cnt++;
 			if (cnt == 4) 
			{
			 cout<<Role[z];
			 printf(" won\n");
			 return ;
			}
		}
 	}
 	
 	int cnt[3]={0,0,0};
 	for (int i=0;i<4;++i)
 	{
 		if (map[i][i] == 'X') cnt[0]++; else
 		if (map[i][i] == 'O') cnt[1]++; else
 		if (map[i][i] == 'T') cnt[2]++;
 	}
 	if (cnt[0] + cnt[2] == 4)
 	{
 			 printf("X won\n");
			 return ;
	} else
	if (cnt[1] + cnt[2] == 4)
 	{
 			 printf("O won\n");
			 return ;
	}
 	cnt[0]=cnt[1]=cnt[2]=0;
 	for (int i=0;i<4;++i)
 	{
 		if (map[i][3-i] == 'X') cnt[0]++; else
 		if (map[i][3-i] == 'O') cnt[1]++; else
 		if (map[i][3-i] == 'T') cnt[2]++;
 	}
 	if (cnt[0] + cnt[2] == 4)
 	{
 			 printf("X won\n");
			 return ;
	} else
	if (cnt[1] + cnt[2] == 4)
 	{
 			 printf("O won\n");
			 return ;
	}
	for (int i=0;i<4;++i)
	for (int j=0;j<4;++j)
	if (map[i][j]=='.')
	{
		printf("Game has not completed\n");
		return ;
	}
		printf("Draw\n");
		return;
}
 int main()
 {
 	int n;
 	freopen("A-large.in","r",stdin);
 	freopen("A-large.txt","w",stdout);
 	cin>>n;
 	for (int i=0;i<n;++i)
 	{
 		for (int j=0;j<4;++j)
 		cin>>map[j];
 		Solve(i+1);		 	
 	}
 	return 0;
 }
