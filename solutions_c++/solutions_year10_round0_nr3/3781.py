#include <vector>
#include <queue>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ");
int ParseInt(std::string& str);
void ReadInput(std::string filename);


int main()
{
	ReadInput("C-small-attempt3.in");

	return 0;
}

void ReadInput(std::string filename)
{
	std::ifstream file(filename.c_str());

	if(!file )
		false;
	std::string buffer;
	std::vector<std::string> tokens;
	
	getline(file, buffer);
	
	Tokenize(buffer, tokens );
	std::vector<std::string>::iterator it= tokens.begin();
	int caseNum= ParseInt(*it);
	tokens.clear();
	std::ofstream output("output.txt");
	for(int i=0; i< caseNum; i++) 
	{
		getline(file, buffer);	
		Tokenize(buffer, tokens );
		it= tokens.begin();
		int Rtimes= ParseInt(*it);
		
		it++;
		int Kpeople= ParseInt(*it);

		it++;
		int Ngruop= ParseInt(*it);
		tokens.clear();

		std::queue<int> groupNums;
		getline(file, buffer);
		Tokenize(buffer, tokens );
		it= tokens.begin();
		while(it!=tokens.end())
		{
			int val = ParseInt(*it++);
			groupNums.push(val);
		}
		tokens.clear();

		int money = 0;
		for(int j=0; j<Rtimes; j++)
		{
			std::queue<int> groupRide;
			int num = groupNums.front();
			int iavailable = Kpeople;
			while(num <= iavailable )
			{
				groupRide.push(num);
				money += num;
				groupNums.pop();
				iavailable -= num;
				if(groupNums.size()<=0)
					break;
				num = groupNums.front();
			}
			int k = groupRide.size();
			while(k)
			{
				int val = groupRide.front();
				groupNums.push(val);
				groupRide.pop();
				k--;
			}
		}
		if(i==caseNum-1)
			output<<"Case #"<<i+1<<": "<<money;
		else
			output<<"Case #"<<i+1<<": "<<money<<std::endl;
	}
}

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters)
{
    // 맨 첫 글자가 구분자인 경우 무시
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // 구분자가 아닌 첫 글자를 찾는다
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // token을 찾았으니 vector에 추가한다
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // 구분자를 뛰어넘는다.  "not_of"에 주의하라
        lastPos = str.find_first_not_of(delimiters, pos);
        // 다음 구분자가 아닌 글자를 찾는다
        pos = str.find_first_of(delimiters, lastPos);
    }
}

int ParseInt(std::string& str){
	int parsingNum = 0;
	int pos =0;
	bool is_negative =false;
	std::string::size_type neg = str.find_first_of("-",0);
	if(neg!=str.npos){
		is_negative = true;
		pos=neg+1;
	}
	for(int i=pos; i<str.size(); i++){
		parsingNum = parsingNum*10 + str[i]-'0';
	}
	if(is_negative)
		return 0-parsingNum;
	else return parsingNum;
}
