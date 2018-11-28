#include <stdio.h>
#include <vector>
#include <algorithm>

char buff[32768];

typedef std::vector<int> t_int_vec;

void get_buff()
{
	buff[0]='\0';
	gets(buff);
	//printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
	return atoi(buff);
}

void get_vector(int len,t_int_vec& v)
{
	get_buff();
	int num;
	char *loc=buff;
	for (int i=0 ; i<len ; ++i)
	{
		num=atoi(loc);
		v.push_back(num);
		loc=strchr(loc,' ')+1;
	}
}

int main(int argc, char* argv[])
{
	int T=get_num();

	for (int i=0 ; i<T ; ++i)
	{
		int n=get_num();
		t_int_vec v1,v2;
		get_vector(n,v1);
		get_vector(n,v2);

		std::sort(v1.begin(),v1.end());
		std::sort(v2.begin(),v2.end());
		int res=0;
		for (int j=0 ; j<n ; ++j)
			res+=v1[j]*v2[n-j-1];
		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}

