
#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;

typedef unsigned int ui;
typedef signed int si;
typedef double dl;


#define fr(a,b,c) for(ui a = (b); a < (c); a++)
#define tr_v(i,v) for(unsigned int i = 0; i < v .size(); i ++)
#define tr(e,v) for(typeof(v.begin()) e = v .begin(); e != v .end(); e ++)
#define named(name) goto name; name##_skip: if(0) name:
#define break(n) goto name:
#define all(c) (c).begin(),(c).end()

void eatBlank()
{
	while(isspace(std::cin.peek()))
		std::cin.get();
}

template<class T> T in()
{
	T t;
	eatBlank();
	std::cin >> t;
	return t;
}

template<> std::string in()
{
	std::string s;
	char c;
	eatBlank();
	while(!isspace(c = std::cin.get()))
		s.append(1,c);
	return s;
}

template<class T> std::vector<T> in(ui n)
{
	std::vector<T> v(n);
	tr_v(i,v)
		v[i] = in<T>();
    return v;
}

void solve()
{
    ui n = in<ui>();
    ui l = in<ui>();
    ui h = in<ui>();

    vector<ui> v = in<ui>(n);
    
    fr(f,l,h+1)
    {
        bool a=true;
        tr_v(i,v)
        {
            if(f%v[i] && v[i]%f)
            {
                a = false;
                break;
            }
        }
        
        if(a)
        {
            std::cout << f;
            return;
        }
    }

    std::cout << "NO";
}

int main()
{
	ui n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(ui i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}
