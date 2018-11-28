#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

string base("QWERASDF");

int index(char to_get)
{
	int index;
	for(index = 0; base[index] != to_get; index++);
	return index;
}

void print(string result)
{
	if(result.empty())
	{
		cout<<"[]";
		return;
	}
	
	cout<<"["<<result[0];
	
	for(size_t cnt = 1; cnt < result.size(); cnt++)
		cout<<", "<<result[cnt];
		
	cout<<"]";	
}

int main(int argc, char *argv[])
{
	FILE *fp = fopen(argv[1],"r");
	
	int tot_cases;
	fscanf(fp,"%d",&tot_cases);
	
	for(int outcnt = 1; outcnt <= tot_cases; outcnt++)
	{
		int tot_prod;
		fgetc(fp);
		fscanf(fp,"%d",&tot_prod);
		
		char buf[4];
		string tempstr = "";
		char tempc = '\0';
		vector<string> lhs(tot_prod*2,tempstr);
		vector<char> rhs(tot_prod*2,tempc);
		
		for(int cnt = 0; cnt < tot_prod*2; cnt+=2)
		{
			fgetc(fp);
			fscanf(fp,"%s",buf);
			
			tempstr = "";
			tempstr += buf[0];
			tempstr += buf[1];
			
			lhs[cnt] = tempstr;
			rhs[cnt] = buf[2];
			
			tempstr = "";
			tempstr += buf[1];
			tempstr += buf[0];
			
			lhs[cnt+1] = tempstr;
			rhs[cnt+1] = buf[2];
		}

		int tot_rej;
		fgetc(fp);
		fscanf(fp,"%d",&tot_rej);
		
		vector<char> rej_list;
		vector<vector<char> > reject(8,rej_list);
		
		for(int cnt = 0; cnt <tot_rej; cnt++)
		{
			fgetc(fp);
			fscanf(fp,"%s",buf);
			
			reject[index(buf[0])].push_back(buf[1]);
			reject[index(buf[1])].push_back(buf[0]);
		}
		
		int strlen;
		fgetc(fp);
		fscanf(fp,"%d",&strlen);
		fgetc(fp);
		
		string result;
		
		for(int cnt = 0; cnt < strlen; cnt++)
		{
			tempc = fgetc(fp);
			bool flag = false;
			
			// Prod Check
			if(result.size() > 0)
			{
				tempstr = "";
				tempstr += result[result.size()-1];
				tempstr += tempc;
				
				size_t incnt;
				for(incnt = 0; incnt < lhs.size(); incnt++)
					if(lhs[incnt].compare(tempstr) == 0)
					{
						flag = true;
						break;
					}
					
				if(flag)
					result[result.size()-1] = rhs[incnt];
			}
			
			// Rej Check
			if(!flag && result.size() > 0)
				for(size_t incnt1 = 0; incnt1 < result.size(); incnt1++)
					for(size_t incnt2 = 0; incnt2 < reject[index(tempc)].size(); incnt2++)
						if(reject[index(tempc)][incnt2] == result[incnt1])
						{
							result = "";
							flag = true;
							break;
						}
						
			// If nothing
			if(!flag)
				result += tempc;
		}
		
		cout<<"Case #"<<outcnt<<": ";
		print(result);
		cout<<endl;
	}

	fclose(fp);

	return 0;
}
