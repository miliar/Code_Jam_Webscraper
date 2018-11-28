#include<iostream>
#include<string.h>

using namespace std;

int main()
{
	int l;
	int d;
	int n;
	cin>>l>>d>>n;
	char str[5000][500];
	char input[500][500];
	int i=0;
	while(i<d)
	{
		cin>>str[i];
		i++;
		
	}
	for(int i=0;i<n;i++)
	cin>>input[i];

	char arr[15][30];
	char name[500];
	
	for(int i=0;i<n;i++)
	{	
		char* s = &name[0];
		char *str_addr = (char*)(&input[i][0]);
		strcpy(s,str_addr);
		for(int p=0;p<l;p++)
		{
			
			if(*s !='(')
			{
				arr[p][0] =*s ;
				arr[p][1] = '\0';
				s += 1;
			}
			else
			{
				//cout<<"Entering else ";
				char *chstart = strchr(s,'(');
				char *chend = strchr(s,')');
				//if((chstart != NULL)&&(chend != NULL))
				{
					strncpy(arr[p],s,(chend - chstart+1));
					arr[p][chend - chstart+1] = '\0';
					s += chend - chstart +1; 
					//cout<<s<<"\n";
				}
			}
				
		}
		//cout<<arr[l-2]<<"\n";
		/*for(int p=0;p<l;p++)
		cout<<arr[p]<<"\n";*/
		
		//cout<<"\n \n \n";
		//printf("%s\n",arr[p]);
		int count =0;
		for(int j=0;j<d;j++)
		{
			int flag =1;
			for(int k =0;k<l;k++)
			{
				if(strchr(arr[k], str[j][k]) == '\0')
				{
					flag =0;
					break;
				}
			}
			if(flag == 1)
			{
				count += 1;
				//cout<<str[j]<<" \n";
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return(0);
}