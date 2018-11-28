#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

class Counter
{
public:
	Counter(string _line) : text("welcome to code jam")
	{
		line = _line;

		line_len = line.length();
		text_len = text.length();

		// Init dynamics
		data.resize(text_len);
		for(size_t i = 0; i<text_len; ++i)
			data[i].resize(line_len, -1);
	}

	int count()
	{
		return get(0, 0);
	}

	int get(int t_pos, int l_pos)
	{
		if(t_pos == text_len)
			return 1;

		if(l_pos == line_len)
			return 0;

		if(data[t_pos][l_pos] == -1) {
			int res = 0;
			for(size_t p = l_pos; p < line_len; ++p) {
				if(line[p] == text[t_pos]) {
					res = (res + get(t_pos+1, p+1)) % 10000;
				}
			}
			data[t_pos][l_pos] = res;
		}
		return data[t_pos][l_pos];
	}

private:
	string text;
	string line;
	vector<vector<int> > data;

	size_t line_len;
	size_t text_len;

};

int main()
{
	size_t N;
	cin>>N;
	char buf[1024];
	cin.getline(buf, 100);
	for(size_t n = 1; n<=N; ++n) {
		cin.getline(buf, 1024);
		string line(buf);


		Counter counter(line);
		cout<<"Case #"<<n<<": ";
		cout.width(4);
		cout.fill('0');
		cout<<counter.count()<<endl;
	}

	return 0;
}
