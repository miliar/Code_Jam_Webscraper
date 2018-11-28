#include<iostream>
#include<cstdlib>

using namespace std;

class A
{
	int value;

public:

	A(int value)
	{
		this->value=10;
		cout<<"\nParameter :"<<value;
		cout<<"\nMember    :"<<this->value;
	}
};
int main()
{
	A a(20);
	system("PAUSE");
	return 0;
}
