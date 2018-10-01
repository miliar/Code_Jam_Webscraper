#!/usr/bin/env python

from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
	for case in range(1, int(f.readline().strip()) + 1):
		limiting_position, limiting_speed = None, None
		distance, count = map(int, f.readline().strip().split())
		for i in range(count):
			position, speed = map(int, f.readline().strip().split())
			if limiting_position is None:
				limiting_position, limiting_speed = position, speed
				continue
			if speed == limiting_speed:
				if position < limiting_position:
					limiting_position, limiting_speed = position, speed
				continue
			cross_time = float(position - limiting_position) / float(limiting_speed - speed)
			cross_distance = position + speed * cross_time
			if cross_time < 0 and position < limiting_position:
				limiting_position, limiting_speed = position, speed
			elif cross_time > 0 and cross_distance > distance and position < limiting_position:
				limiting_position, limiting_speed = position, speed
			elif cross_time > 0 and cross_distance < distance and position > limiting_position:
				limiting_position, limiting_speed = position, speed
		finish_time = float(distance - limiting_position) / limiting_speed
		print("Case #%s: %.6f" % (case, distance / finish_time))