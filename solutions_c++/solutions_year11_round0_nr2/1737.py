#include <iostream>
#include <vector>
#include <string>

std::string combine(std::string in, char a, char b, char n)
{
	unsigned int l = in.length();
	if(l >= 2)
	{
		if(in[l-1] == b
		&& in[l-2] == a)
		{
			in[l-2] = n;
			in.resize(l-1);
		}
	}
	return in;
}

std::string combine(const std::string& in, std::string key)
{
	std::string r = combine(in, key[0], key[1], key[2]);
	if(r == in)
		r = combine(in, key[1], key[0], key[2]);
	return r;
}

std::string oppose(std::string in, char a, char b)
{
	unsigned int l = in.length();
	unsigned int i = l-1;
	while(i < l && in[i] != a)
		i--;

	unsigned int j = i-1;
	while(j < l && in[j] != b)
		j--;

	if(i < l && j < l)
		return ""; //in.erase(j, i - j + 1);
	return in;
}

std::string oppose(const std::string& in, std::string key)
{
	std::string r = oppose(in, key[0], key[1]);
	if(r == in)
		r = oppose(in, key[1], key[0]);
	return r;
}

std::vector<std::string> cbkey;
std::vector<std::string> opkey;

void readVec(std::vector<std::string> & v, unsigned int l)
{
	unsigned int n;
	std::cin >> n;

	for(unsigned int i=0; i < n; i++)
	{
		while(std::cin.peek() == ' ')
			std::cin.get();
		
		std::string s;
		for(unsigned int j=0; j < l; j++)
			s += (char)std::cin.get();
		
		v.push_back(s);
	}
}

std::string transform(std::string in)
{
	for(unsigned int i=0; i < cbkey.size(); i++)
		in = combine(in, cbkey[i]);
	for(unsigned int i=0; i < opkey.size(); i++)
		in = oppose(in, opkey[i]);

	return in;
}

void solve()
{
	readVec(cbkey,3);
	readVec(opkey,2);

	unsigned int n = 0;
	std::cin >> n;

	
	while(std::cin.peek() == ' ')
		std::cin.get();

	std::string in;

	for(unsigned int i=0; i < n; i++)
	{
		in.append(1,(char)std::cin.get());
		in = transform(in);
	}

	std::cout << '[';
	if(in.length())
	{
		for(unsigned int i=0; ({ std::cout << in[i]; i < in.length() - 1; }); i++)
			std::cout << ", ";
	}
	std::cout << ']';

	while(std::cin.peek() == ' ')
		std::cin.get();
	std::cin.get();

	cbkey.clear();
	opkey.clear();
}


int main()
{
	unsigned int n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(unsigned int i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}

