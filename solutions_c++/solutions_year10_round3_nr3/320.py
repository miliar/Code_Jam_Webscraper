#include <iostream>

using namespace std;

int main()
{
	int T, M, N;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cin >> M >> N;
		int bark[M][N];
		char c;
		for (int j=0; j<M; j++)
		{
			int r=0;
			for (int k=0; k<N/4; k++)
			{
				cin >> c;
				switch (c)
				{
					case '0': bark[j][r++] = 0; 
					 bark[j][r++] = 0; bark[j][r++] = 0;   bark[j][r++] =0; break;
case '1':  bark[j][r++] =0;  bark[j][r++] =0;  bark[j][r++] =0;  bark[j][r++] =1; break;
case '2': bark[j][r++] =0;  bark[j][r++] =0;  bark[j][r++] =1; bark[j][r++] =0; break;
case '3':  bark[j][r++] =0;  bark[j][r++] =0;  bark[j][r++] =1;  bark[j][r++] =1; break;
case '4': bark[j][r++] = 0;  bark[j][r++] = 1; bark[j][r++] = 0;   bark[j][r++] =0; break;
case '5':  bark[j][r++] =0;  bark[j][r++] =1;  bark[j][r++] =0;  bark[j][r++] =1; break;
case '6': bark[j][r++] =0;  bark[j][r++] =1;  bark[j][r++] =1; bark[j][r++] =0; break;
case '7':  bark[j][r++] =0;  bark[j][r++] =1;  bark[j][r++] =1;  bark[j][r++] =1; break;
case '8': bark[j][r++] = 1;  bark[j][r++] = 0; bark[j][r++] = 0;   bark[j][r++] =0; break;
case '9':  bark[j][r++] =1;  bark[j][r++] =0;  bark[j][r++] =0;  bark[j][r++] =1; break;
case 'A': bark[j][r++] =1;  bark[j][r++] =0;  bark[j][r++] =1; bark[j][r++] =0; break;
case 'B':  bark[j][r++] =1;  bark[j][r++] =0;  bark[j][r++] =1;  bark[j][r++] =1; break;
case 'C': bark[j][r++] = 1;  bark[j][r++] = 1; bark[j][r++] = 0;   bark[j][r++] =0; break;
case 'D':  bark[j][r++] =1;  bark[j][r++] =1;  bark[j][r++] =0;  bark[j][r++] =1; break;
case 'E': bark[j][r++] =1;  bark[j][r++] =1;  bark[j][r++] =1; bark[j][r++] =0; break;
case 'F':  bark[j][r++] =1;  bark[j][r++] =1;  bark[j][r++] =1;  bark[j][r++] =1; break;

  	
				}
			}
			//cin>>c;
		}
		
		int small = M;
		if (N<M) small = N;
		int boards[33] = {0};
		for (int len=small; len>=1; len--)
		{
			for (int p=0; p+len<=M; p++)
				for (int q=0; q+len<=N; q++)
				{
				//	cout <<"Testing " << len << " " << p << " " << q << endl;
					bool nikala = false;
					bool flag = true;
					int pow=len-1;
					int s=0;
					for(int c=q; c<q+len && !nikala; c++)
					{
						pow=len-1;
						s=0;
						for(int b=p; b<p+len && !nikala; b++)
						{
							if (bark[b][c] == -1) nikala=true;
							s+= bark[b][c]*(1<<pow);
							pow--;
						}
						int f = s>>1; //, g = s<<1;
						int ff = ~(s ^ f); //, gg = ~(s ^ g);
						if (!nikala && ((ff%(1<<len) != 0 && s/(1<<(len-1))!=0)  || (ff%(1<<(len-1)) !=0 && s/(1<<(len-1))==0)))
							flag=false;
					}

					pow=len-1;
					s=0;
					//for(int c=p; c<p+len && !nikala; c++)
					//{
						pow=len-1;
						s=0;
						for(int b=q; b<q+len && !nikala; b++)
						{
							s+= bark[p][b]*(1<<pow);
							pow--;
						}
						int f = s>>1;//, g = s<<1;
						int ff = ~(s ^ f);//, gg = ~(s ^ g);
					//	if ((ff%(1<<len) != 0 || gg%(1<<len) !=0) && !nikala)
						if (!nikala && ((ff%(1<<len) != 0 && s/(1<<(len-1))!=0)  || (ff%(1<<(len-1)) !=0 && s/(1<<(len-1))==0)))
							flag=false;
					//}

					if (flag && !nikala) {
				//	cout << "FOUND! " << len << " " << p << " " << q << endl;
					boards[len]++;
					for(int a=p; a<p+len; a++)
						for(int z=q; z<q+len; z++)
							bark[a][z]=-1;

					}
				}	
		}

		int dif=0;
		for (int t=1; t<=small; t++)
			if (boards[t] > 0) dif++;
		cout << "Case #" << i+1 << ": " << dif << endl;
		for(int t=small; t>=1; t--)
			if (boards[t] > 0) cout << t << " " << boards[t] << endl;

	}
}
