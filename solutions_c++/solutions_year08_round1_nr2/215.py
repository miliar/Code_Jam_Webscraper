#include <stdio.h>
#include <list>
#include <set>

#define NO_MALTED 0

char buff[32768];

typedef std::set<int> t_int_set;

struct s_customer_info
{
	s_customer_info() { malted_flavour=NO_MALTED; }
	int malted_flavour;
	t_int_set unmalted_flavours;
};

typedef std::list<s_customer_info> t_customers;

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

int get_next_num(char **loc)
{
	int num=atoi(*loc);
	*loc=strchr(*loc,' ')+1;
	return num;
}

void get_customer_info(s_customer_info& i)
{
	get_buff();
	char *loc=buff;
	int len=get_next_num(&loc);
	for (int j=0 ; j<len ; ++j)
	{
		int flavour=get_next_num(&loc);
		int malted=get_next_num(&loc);
		if (malted)
			i.malted_flavour=flavour;
		else
			i.unmalted_flavours.insert(flavour);
	}
}

int main(int argc, char* argv[])
{
	int C=get_num();

	for (int i=0 ; i<C ; ++i)
	{
		int N=get_num();
		int M=get_num();
		t_customers customers;

		for (int j=0 ; j<M ; ++j)
		{
			s_customer_info i;
			get_customer_info(i);
			customers.push_back(i);
		}

		t_int_set malted;
		bool impossible=false;
		bool changed=true;
		while (!customers.empty() && !impossible && changed)
		{
			changed=false;
			
			for (t_customers::iterator c_iter=customers.begin(),c_eiter=customers.end() ; c_iter!=c_eiter ; ++c_iter)
			{
				s_customer_info& i=*c_iter;

				for (t_int_set::iterator um_iter=i.unmalted_flavours.begin(), um_eiter=i.unmalted_flavours.end() ; um_iter!=um_eiter ; )
				{
					if (malted.count(*um_iter))
						um_iter=i.unmalted_flavours.erase(um_iter);
					else
						++um_iter;
				}

				if (i.malted_flavour!=NO_MALTED && i.unmalted_flavours.empty())
				{
					if (malted.insert(i.malted_flavour).second)
						changed=true;
				}

				if (i.unmalted_flavours.empty() && i.malted_flavour==NO_MALTED)
					impossible=true;
			}
		}

		printf("Case #%d:",i+1);
		if (impossible)
			printf(" IMPOSSIBLE");
		else
		{
			for (int j=0 ; j<N ; ++j)
				printf(" %d",malted.count(j+1));
		}
		printf("\n");
	}

	return 0;
}

