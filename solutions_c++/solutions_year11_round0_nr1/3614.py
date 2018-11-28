/*
 * Robot.cpp
 *
 *  Created on: May 7, 2011
 *      Author: m1cRo
 */

#include "Robot.h"

Robot::Robot(unsigned int currentPosition, Hallway::ENUM_HALLWAY_TYPE holeType) {
	_currentPosition=currentPosition;
	_holeType=holeType;
}

void Robot::executeStep(std::vector<Button>& buttons){
	if(!buttons.empty()){
		Hallway::ENUM_HALLWAY_TYPE buttonType=buttons[0].getHoleType();
		if(buttonType==_holeType){
			unsigned int currentPosition=buttons[0].getButtonPosition();
			if(currentPosition==_currentPosition){
				buttons.erase(buttons.begin(),buttons.begin()+1);
			}else{
				if(currentPosition>_currentPosition){
					_currentPosition++;
				}else{
					_currentPosition--;
				}
			}
		}else{
			std::vector<Button>::iterator currentButton;
			for(currentButton=buttons.begin(); currentButton!=buttons.end();currentButton++){
				if(currentButton->getHoleType()==_holeType){
					if(_currentPosition<currentButton->getButtonPosition()){
						_currentPosition++;
					}else if(_currentPosition>currentButton->getButtonPosition()){
						_currentPosition--;
					}

					break;
				}
			}
		}
	}
}

Robot::~Robot() {
	// TODO Auto-generated destructor stub
}
