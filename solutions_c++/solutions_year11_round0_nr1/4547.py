#include <cstdio>
#include <iostream>
#include <stdlib.h>
#include <deque>
#include <sstream>
using namespace std;

struct Task
{
  char bot_;
  int button_;
};

const Task* getNextTask(const std::deque<Task>& tasks, char bot='0')
{
  if (tasks.size() == 0) return 0;

  if ( bot == '0' )
    return &tasks[0];
  else 
    {
      for (int i = 0; i < int(tasks.size()); ++i)
	if (tasks[i].bot_ == bot) return &tasks[i];
    }

  return 0;
}


int main ()
{
  ostringstream debugout;
  ostringstream finalout;
  
  int T, TC = 1, N;

  for (scanf ("%d", &T); TC <= T; TC++)
    {
      debugout << "case " << TC << std::endl;
      finalout << "Case #" << TC << ": ";

      scanf ("%d", &N);
      // read in tasks for the robots
      std::deque<Task> tasks;
      for (int task = 0; task < N; ++task)
	{
	  tasks.push_back(Task());
	  scanf(" %c %d",&tasks.back().bot_,&tasks.back().button_);
	  debugout << "task is " << tasks.back().bot_ << " " << tasks.back().button_ << std::endl;
	}

      const Task* task = getNextTask(tasks);
      const Task* btask = getNextTask(tasks,'B');
      const Task* otask = getNextTask(tasks,'O');
      int bpos = 1;
      int opos = 1;

      int t;
      for (t = 0; task; ++t)
	{
	  debugout << "t=" << t+1;
	  // let each robot work towards its goal
	  bool bmoved = false;
	  bool omoved = false;
	  if ( btask && btask->button_ != bpos )
	    {
	      bpos = bpos + ( btask->button_ > bpos ? 1 : -1 );
	      debugout << "\tB moves to " << bpos;
	      bmoved = true;
	    }
	  if ( otask && otask->button_ != opos )
	    {
	      opos = opos + ( otask->button_ > opos ? 1 : -1 );
	      debugout << "\tO moves to " << opos;
	      omoved = true;
	    }

	  // finish tasks
	  if ( btask && !bmoved && task == btask && btask->button_ == bpos )
	    {
	      debugout << "\tB pushes " << bpos;
	      tasks.pop_front();
	      task = getNextTask(tasks);
	      btask = getNextTask(tasks,'B');
	      if (task)
		debugout << " task is now " << task->bot_ << " " << task->button_;
	    }
	  else if ( !omoved && otask && task == otask && otask->button_ == opos)
	    {
	      debugout << "\tO pushes " << opos;
	      tasks.pop_front();
	      task = getNextTask(tasks);
	      otask = getNextTask(tasks,'O');
	      if (task)
		debugout << " task is now " << task->bot_ << " " << task->button_;
	    }
	  debugout << std::endl;
	}
      
      finalout << t << std::endl;
    }

  std::cout << finalout.str();
  // std::cout << " ----- " << std::endl;
  // std::cout << debugout.str();

    return 0;
}
