#include <iostream>
#include <fstream>
#include <string>
#include <queue>


int main(int argc, char** argv)
{
	std::ifstream input(argv[1],std::ios_base::in);
	std::ofstream output(argv[2],std::ios_base::out);
	int caseNum;
	input>>caseNum;
	//std::cout<<caseNum<<std::endl;
	for(int i = 0; i<caseNum; ++i)
	{
		int count;
		std::queue<int> blue;
		std::queue<int> orange;
		std::queue<char> button;
		input>>count;
		//std::cout<<count;
		for(int btn = 0; btn < count; ++btn)
		{
			char c;
			input>>c;
			int i;
			input>>i;
			//std::cout<<"c:"<<c<<" i:"<<i<<"\n";
			if(c == 'O')
			{
				orange.push(i);
				button.push('O');
				continue;
			}
			if(c == 'B')
			{
				blue.push(i);
				button.push('B');
				continue;
			}
		}
		/*
		while(!button.empty()){
			std::cout<<button.front();
			button.pop();
		}
		std::cout<<"\n";

		*/
		
		int seconds = 0;
		int b_pos = 1;
		int o_pos = 1;
		bool pressed = false;
		while(!button.empty())
		{
			if((!button.empty()) && (button.front() == 'B') && (blue.front() == b_pos))
			{
				button.pop();
				blue.pop();
				pressed = true;
				//std::cout<<"Blue pressed\n";
			}
			else if(!blue.empty() && blue.front()>b_pos){
				++b_pos;
				//std::cout<<"B++\n";
			}
			else if(!blue.empty() && blue.front()<b_pos){
				--b_pos;
				//std::cout<<"B--\n";
			}


			if((!button.empty()) && (button.front() == 'O') && (orange.front() == o_pos) && (pressed == false))
			{
				button.pop();
				orange.pop();
				//std::cout<<"Orange pressed\n";
			}
			else if(!orange.empty() && orange.front()>o_pos){
				++o_pos;
				//std::cout<<"O++\n";
			}
			else if(!orange.empty() && orange.front()<o_pos){
				//std::cout<<"O--\n";
				--o_pos;
			}


			pressed = false;
			//std::cout<<seconds<<"\n\n";
			++seconds;
		}
		output<<"Case #"<<i+1<<": "<<seconds<<"\n";

	}
	system("pause");

}