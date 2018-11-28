#!/bin/bash

NINPUTS=`cat input | head -1`

IFS=$'\n'
j=1
for i in `cat input | tail -n $NINPUTS`
do
    RESULT=`./solve "$i"`
    echo 'Case #'$j: $RESULT
    j=$(($j + 1))
done