#include <fstream>
#include <vector>
//#include <iostream>

class robot
{
private:
	int position;
public:
	robot(int x)
	{
		position=x;
	}
	
	unsigned long long int move(int target, unsigned long long int time)
	{
		if(target>position)
		{
			if(target-position<=time)
			{
				position=target;
				return time-(target-position);
			}
			else
			{
				position+=time;
				return 0;
			}
		}
		else
		{
			if(position-target<=time)
			{
				position=target;
				return time-(position-target);
			}
			else
			{
				position-=time;
				return 0;
			}
		}
	}
	
	unsigned long long int press(int z)
	{
		if(position==z)
		{
			return 1;
		}
		else
		{
			if(z>position)
			{
				unsigned long long int temp=position;
				position=z;
				return z-temp+1;
			}
			else
			{
				unsigned long long int temp=position;
				position=z;
				return temp-z+1;
			}
		}
	}
	
	int pos()
	{
		return position;
	}
	
	void reset()
	{
		position=0;
	}
	
};

int main()
{
	std::ifstream in("robots.in");
	std::ofstream out("robots.out");
	int T;
	in >> T;
	
	for(int i=1; i<=T; ++i)
	{
		out << "Case #" << i << ": ";
		int N;
		in >> N;
		unsigned long long int time=0;
		unsigned long long int result=0;
		char old=' ';
		robot blue(1);
		robot orange(1);
		
		for(int i=0; i<N; ++i)
		{
			char kirjain;
			in >> kirjain;
			int numero;
			in >> numero;
			
			
			if(kirjain=='B') /// SININEN
			{
				if(kirjain==old)
				{	
					unsigned long long int temp = blue.press(numero);
					time += temp;
					result += temp;
				}
				else
				{
					blue.move(numero, time);
					time=blue.press(numero);
					result += time;
				}
			}
			else /// ORANSSI
			{
				if(kirjain==old)
				{
					unsigned long long int temp = orange.press(numero);
					time += temp;
					result += temp;
				}
				else
				{
					orange.move(numero, time);
					time=orange.press(numero);
					result += time;
				}
			}
			
			old=kirjain;
		}
		
		out << result << std::endl;
		
	}
	
}







