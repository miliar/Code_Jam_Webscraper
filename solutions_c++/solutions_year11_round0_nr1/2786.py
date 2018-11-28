#include "Robot.h"

// ----------------------------------------------------------------------------
// Robot
// ----------------------------------------------------------------------------
Robot::Robot()
{
  cur_idx = 0;;
  max_idx = 0;
  cur_pos = 0;
  for (int i = 0; i < MAX_N; i++) to_do_list[i] = -1;
}

Robot::~Robot()
{
}

bool Robot::move()
{
  int next_pos = to_do_list[cur_idx];
  if (cur_pos < next_pos)
  {
    cur_pos++;
    return true;
  } else
  if (cur_pos > next_pos)
  {
    cur_pos--;
    return true;
  }
  return false;
}

bool Robot::pressable()
{
  return cur_pos == to_do_list[cur_idx];
}

bool Robot::press_button()
{
  if (!pressable()) return false; // for test
  cur_idx++;
  return true;
}

// ----------------------------------------------------------------------------
// RobotMgr
// ----------------------------------------------------------------------------
RobotMgr::RobotMgr()
{
  cur_idx = 0;
  max_idx = 0;
  for (int i = 0; i < MAX_N; i++)
  {
    to_do_type[MAX_N] = ORANGE; // meaningless
    to_do_list[MAX_N] = -1;
  }
}

RobotMgr::~RobotMgr()
{
}

void RobotMgr::prepare()
{
  for (int i = 0; i < max_idx; i++)
  {
    RobotType rt = to_do_type[i];
    switch ( rt )
    {
    case ORANGE:
      robot[0].to_do_list[robot[0].max_idx] = to_do_list[i];
      robot[0].max_idx++;
      break;
    case BLUE:
      robot[1].to_do_list[robot[1].max_idx] = to_do_list[i];
      robot[1].max_idx++;
      break;
    }
  }
  elapsed = 0;
}

void RobotMgr::process()
{
  Robot* this_robot, * other_robot;

  if (to_do_type[cur_idx] == 0)
  {
    this_robot = &robot[0];
    other_robot = &robot[1];
  } else
  {
    this_robot = &robot[1];
    other_robot = &robot[0];
  }

  if (this_robot->pressable())
  {
    this_robot->press_button();
    cur_idx++;
  } else
  {
    this_robot->move();
  }
  other_robot->move();

  elapsed++;
}

bool RobotMgr::completed()
{
  return cur_idx == max_idx;
}


