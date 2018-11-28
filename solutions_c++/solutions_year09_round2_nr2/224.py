#include <iostream>
#include <string>
#include <algorithm>
#include <boost/lexical_cast.hpp>
int main()
{
    int n;
    std::cin >> n;
    std::string s;
    std::getline(std::cin, s);
    for (int i=0;i<n;++i)
    {
        std::getline(std::cin, s);
        s="0" + s;
        int l1 =0,l2 = 0;
        //l1 = boost::lexical_cast<long long>(s);
        std::next_permutation(s.begin(), s.end());
        //l2 = boost::lexical_cast<long long>(s);
        int j =0;
        while (s[j]=='0') j++;
        //std::cout<< "Case #"<<i+1<<": "<<l1<<","<<l2<<"\n";
        std::cout<< "Case #"<<i+1<<": "<<(char*)(s.c_str()+j)<<"\n";
    }
}
