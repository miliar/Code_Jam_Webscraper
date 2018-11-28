// bot_trust.cpp : Defines the entry point for the console application.
//
#include <tchar.h>

#include <iostream>
#include <vector>
#include <cassert>
#include <fstream>

struct command {
  command *pv;
  command *nx;

  bool completed;
  char bot;
  int position;

  command(command *pv, command *nx, char bot, int position)
    : pv(pv), nx(nx), completed(false), bot(bot), position(position) {
      if(pv != 0)
        pv->nx = this;
      if(nx != 0)
        nx->pv = this;
  }
};

using namespace std;

void advance_bot(vector<command*>& olist, int& opos, bool o_pv_complete){
  if(olist.size() > 0){
    command& ocmd = *olist[0];
    if(ocmd.position == opos){

      if(o_pv_complete){
        ocmd.completed = true;
        olist.erase(olist.begin());
        //cerr << ocmd.bot << ": pushed " << ocmd.position << endl;
      }
      else
        ;//cerr << ocmd.bot << ": waiting" << endl;
    }
    else {
      if(ocmd.position < opos)
        opos--;
      else
        opos++;
      //cerr << ocmd.bot << ": now at " << opos << endl;
    }
  }
}

bool is_pv_complete(vector<command*> olist){
  if(olist.size() == 0)
    return true;

  command& cmd = *olist[0];
  if(cmd.pv == 0)
    return true;

  return cmd.pv->completed;
}

int _tmain(int argc, _TCHAR* argv[])
{
  ifstream ifile(argv[1]);
  int ncases;
  ifile >> ncases;

  for(int icase = 0; icase < ncases; ++icase){
    int ncmd;

    command *head = 0, *cmd;
    vector<command*> olist;
    vector<command*> blist;

    ifile >> ncmd;
    for(int icmd = 0; icmd < ncmd; ++icmd){
      char bot;
      int position;

      ifile >> bot >> position;

      if(head == 0)
        cmd = head = new command(0, 0, bot, position);
      else
        cmd = new command(cmd, 0, bot, position);

      if(cmd == 0){
        cout << "out of memory" << endl;
        return 1;
      }

      if(cmd->bot == 'O')
        olist.push_back(cmd);
      else if(cmd->bot == 'B')
        blist.push_back(cmd);
      else
        assert(false);
    }

    int opos = 1, bpos = 1;
    int nsec = 0;
    while(olist.size() != 0 || blist.size() != 0){
      nsec++;
      bool o_pv_complete = is_pv_complete(olist);
      bool b_pv_complete = is_pv_complete(blist);
      advance_bot(olist, opos, o_pv_complete);
      advance_bot(blist, bpos, b_pv_complete);
    }

    cout << "Case #" << icase + 1 << ": " << nsec << endl;
    for(cmd = head; cmd != 0;){
      command *nx = cmd->nx;
      delete cmd;
      cmd = nx;
    }
  }

	return 0;
}

