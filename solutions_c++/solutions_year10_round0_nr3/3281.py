#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;


int main()
{

	ifstream ifile("C-small-attempt2.in");
	ofstream ofile("C-small-attempt2.in-out.txt");
	//ifstream ifile("test.txt");
	//ofstream ofile("test-out.txt");
	
	int times;//С��50������

	long r;//һ������ЩȦ
	long n;//����
	long k; //����޳�
	long i,j;//һ��n�顣
	long f[11];
	long t[11];
	long h[11];//��f[1]�ǵ�f[n],h[n]��¼����
	long score=0;
	
	ifile>>times;
	
	for (i=0;i<times;i++)
	{
		//n devices,and k knock times 
		ifile>>r>>k>>n;
		//����ÿ������,ÿ���ж��ٸ�
		long sum =0;
		for (j=1;j<=n;j++)
		{
			ifile>>f[j];
			sum+=f[j];
		}
		if (sum<=k)
		{
			ofile<<"Case #" <<i+1<<": "; 
			
			ofile<<sum*r<<endl;
		}
		else
		{
			//��ʼ����������
			for (j=1;j<=n;j++)
			{
				//f[n]��¼ȡ������h[n]��¼��n��ʼҪ�ü���
				if (j==1)
				{
					t[j]=1; //��j��һֱ�õ�t[j]��
					h[j]=f[j];
					while(h[j]+f[(t[j])%n+1]<=k)
					{
						t[j]=(t[j])%n+1;
						h[j] = h[j]+f[t[j]];
					}
				}
				else
				{
					if (t[j-1]<j)
					{
						t[j]=j;
						h[j]=f[j];
					}
					else
					{
						t[j]=t[j-1];
						h[j]=h[j-1]-f[j-1];
					}
					while (h[j]+f[t[j]%n+1]<=k)
					{
						t[j]=(t[j])%n+1;
						h[j] = h[j]+f[t[j]];
					}
				}
				
			}
			
			score =0;
			long cur =1;
			for (j=1;j<=r;j++)//һ����ô��Ȧ
			{
				score += h[cur];
				cur = t[cur]%n+1;
			}
			
			
			ofile<<"Case #" <<i+1<<": "; 
			
			ofile<<score<<endl;

		}
	
			
	}
	return 0;
	
}


