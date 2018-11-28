#include <iostream>
#include <queue>
#include <string>
#include <stdio.h>
#include <time.h>

using namespace std;

struct button
{
  int number;
  int order;
};
int solution(queue<button>, queue<button>, int);

int main()
{
  int dataSets;
  scanf("%d", &dataSets);
  
  for(int i = 0; i<dataSets; i++)
    {
      queue<button> blueBot, orangeBot;
      char whiteSpace;
      button button_;
      int buttonNo;
      scanf("%d", &buttonNo);
      for(int j = 0; j<buttonNo; j++)
	{
	  button button_;
	  char bot;
	  int number_;
	  button_.order=j;
	  scanf("%c", &whiteSpace);
	  scanf("%c", &bot);
	  scanf("%c", &whiteSpace);
	  scanf("%d", &button_.number);
	  //cout << bot << " " << button_.number << " " << flush;
	  if (bot == 'O') orangeBot.push(button_);
	  else blueBot.push(button_);
	}
      cout << "Case #" << i + 1 << ": "<< flush;
      cout << solution(orangeBot, blueBot, buttonNo) << endl;
    }
  return 0;
}

int solution(queue<button> orangeBot, queue<button> blueBot, int buttonNo)
{
  bool orangeDone, blueDone;
  int orangePos, bluePos, time, order_;
  
  orangePos = 1;
  bluePos = 1;
  time = 0;
  order_ = 0;
  bool orangeAtButton, blueAtButton;
  orangeAtButton = blueAtButton = 0;
  while(order_ < buttonNo)
    {
      if(!orangeBot.empty()&&orangeBot.front().order==order_&&orangeBot.front().number==orangePos) orangeAtButton = 1;
      if(!blueBot.empty()&&blueBot.front().order==order_&&blueBot.front().number==bluePos) blueAtButton = 1;
      
      if(orangeBot.front().number>orangePos) orangePos++;
      else if(orangeBot.front().number<orangePos) orangePos--;
      if(blueBot.front().number>bluePos) bluePos++;
      else if(blueBot.front().number<bluePos) bluePos--;
      if(orangeAtButton)
	{
	  order_++;
	  orangeBot.pop();
	}
      if(blueAtButton)
	{
	  order_++;
	  blueBot.pop();
	}
      orangeAtButton = blueAtButton = 0;
      
      time++;
    }
  return time;
}
